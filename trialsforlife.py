import sys
import sounddevice as sd
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QMessageBox
from playsound import playsound
from scipy.io.wavfile import read, write
from powerbar import PowerBar
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.axes_grid import make_axes_locatable
from threading import Thread
import logging
from main import Ui_MainWindow
from pyqtgraph.examples.optics import ParamObj
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(filename=" Musical Instruments Emphasizer Logger.log", level=logging.DEBUG,
                    format='%(asctime)s:%(funcName)s:%(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


class GuitarString:
    def __init__(self, pitch, starting_sample, sampling_freq, stretch_factor):
        """Inits the guitar string."""
        self.pitch = pitch
        self.starting_sample = starting_sample
        self.sampling_freq = sampling_freq
        self.stretch_factor = stretch_factor
        self.init_wavetable()
        self.current_sample = 0
        self.previous_value = 0

    def init_wavetable(self):
        """Generates a new wavetable for the string."""
        piano_wavetable_size = self.sampling_freq // int(self.pitch)
        self.guitar_wavetable = (2 * np.random.randint(0, 2, piano_wavetable_size) - 1).astype(float)

    def get_sample(self):
        """Returns next sample from string."""
        if self.current_sample >= self.starting_sample:
            current_sample_mod = self.current_sample % self.guitar_wavetable.size
            drawn_samples = np.random.binomial(1, 1 - 1 / self.stretch_factor)
            if drawn_samples == 0:
                self.guitar_wavetable[current_sample_mod] = 0.5 * (
                        self.guitar_wavetable[current_sample_mod] + self.previous_value)
            sample = self.guitar_wavetable[current_sample_mod]
            self.previous_value = sample
            self.current_sample += 1
        else:
            self.current_sample += 1
            sample = 0

        return sample


class ApplicationWindow(QtWidgets.QMainWindow):
    song_data = []
    vol = 1
    drum_and_guitar_sampleRate = 8000
    piano_Samplerate = 44100  # Hz
    wavetable_size = 200
    gains = np.array([1.0, 1.0, 1.0, 1.0, 1.0])  # to store the gain of each slider
    levels_min = [0, 500, 2000, 1000, 5000]
    levels_max = [500, 1000, 5000, 2000, 10000]
    isPaused = False
    step = 0
    step_right = 0
    drum_keys = ["TNN", "DOM"]
    piano_Keys = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'EgB', 'DfA', 'AcE', 'BDf', 'gAc', 'fAc']
    guitar_strings = ["String1", "String2", "String3", "String4"]
    base_freq = 261.63
    freqs = [98, 123, 147, 196]
    unit_delay = 1000
    drum_volume = 0.5
    guitar_volume = 0.5

    def __init__(self):
        self.note_freqs = {self.piano_Keys[element_num]: self.base_freq * pow(2, (element_num / 12))
                           for element_num in range(12)}

        self.delays = [self.unit_delay * frequency for frequency in range(len(self.freqs))]

        self.stretch_factors = [2 * f / 98 for f in self.freqs]

        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.generatedVolumes = [self.ui.drumslider, self.ui.sliderguitar]
        self.generatedVolumes[0].sliderReleased.connect(self.set_drumVolume)
        self.generatedVolumes[1].sliderReleased.connect(self.set_guitarVolume)

        self.slider_arr = [self.ui.DrumsSlider, self.ui.ViolinSlider, self.ui.FluteSlider,
                           self.ui.PianoSlider, self.ui.XylophoneSlider]
        for i in range(len(self.slider_arr)):
            self.connect_sliders(i)

        self.ui.LoadButton.clicked.connect(self.load)
        self.ui.PlayButton.clicked.connect(self.play)
        self.ui.powerbar.valueChanged.connect(self.Set_Volume)

        self.th = {}  # to be filled with the name of the sound files

        self.ui.c4.clicked.connect(self.generate)
        self.ui.d4.clicked.connect(self.generate)
        self.ui.e4.clicked.connect(self.generate)
        self.ui.f4.clicked.connect(self.generate)
        self.ui.g4.clicked.connect(self.generate)
        self.ui.a4.clicked.connect(self.generate)
        self.ui.b4.clicked.connect(self.generate)
        self.ui.c5.clicked.connect(self.generate)
        self.ui.d5.clicked.connect(self.generate)
        self.ui.e5.clicked.connect(self.generate)
        self.ui.f5.clicked.connect(self.generate)
        self.ui.g5.clicked.connect(self.generate)
        self.ui.a5.clicked.connect(self.generate)
        self.ui.b5.clicked.connect(self.generate)
        self.ui.c6.clicked.connect(self.generate)

        # These are the black keys
        self.ui.c40.clicked.connect(self.generate)
        self.ui.c50.clicked.connect(self.generate)
        self.ui.d40.clicked.connect(self.generate)
        self.ui.d50.clicked.connect(self.generate)
        self.ui.f40.clicked.connect(self.generate)
        self.ui.f50.clicked.connect(self.generate)
        self.ui.g40.clicked.connect(self.generate)
        self.ui.g50.clicked.connect(self.generate)
        self.ui.a40.clicked.connect(self.generate)
        self.ui.a50.clicked.connect(self.generate)
        self.ui.String1.clicked.connect(self.generate)
        self.ui.String2.clicked.connect(self.generate)
        self.ui.String3.clicked.connect(self.generate)
        self.ui.String4.clicked.connect(self.generate)
        self.ui.DR1.clicked.connect(self.generate)
        self.ui.DR2.clicked.connect(self.generate)

    def set_drumVolume(self):
        self.drum_volume = self.generatedVolumes[0].value() / 10

    def set_guitarVolume(self):
        self.guitar_volume = self.generatedVolumes[1].value() / 10

    def get_wave(self, freq, duration=0.5):
        amplitude = 4096
        wave_x_axis = np.linspace(0, duration, int(self.piano_Samplerate * duration))
        wave = amplitude * np.sin(2 * np.pi * freq * wave_x_axis)
        return wave

    def get_song_data(self, music_note):

        if len(self.ui.mw.sender().objectName()) > 1:
            genereted_tune = self.get_chord_data(self.ui.mw.sender().objectName())

        else:
            genereted_tune = [self.get_wave(self.note_freqs[music_note])]
            genereted_tune = np.concatenate(genereted_tune)

        genereted_tune = genereted_tune * (16300 / np.max(genereted_tune))

        return genereted_tune.astype(np.int16)

    def get_chord_data(self, chords):
        chords = chords.split('-')

        chord_data = []
        for chord in chords:
            key_data = sum([self.get_wave(self.note_freqs[piano_key]) for piano_key in list(chord)])
            chord_data.append(key_data)

        chord_data = np.concatenate(chord_data, axis=0)

        return chord_data.astype(np.int16)

    def karplus_strong_drum(self, drum_wavetable, n_samples, probability):
        """Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."""
        samples = []
        current_sample = 0
        previous_value = 0
        while len(samples) < n_samples:
            drawn_samples = np.random.binomial(1, probability)
            sign = float(drawn_samples == 1) * 2 - 1
            drum_wavetable[current_sample] = sign * 0.5 * (drum_wavetable[current_sample] + previous_value)
            samples.append(drum_wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % drum_wavetable.size
        drum_norm = samples / max(samples)
        samples = self.drum_volume * drum_norm
        return np.array(samples)

    def generate(self):
        if self.ui.mw.sender().objectName() in self.piano_Keys:
            key_or_chord_data = self.get_song_data(self.ui.mw.sender().objectName())
            sd.play(key_or_chord_data, self.piano_Samplerate)

        elif self.ui.mw.sender().objectName() in self.drum_keys:
            drum_wavetable = np.ones(self.wavetable_size)
            if self.ui.mw.sender().objectName() == "TNN":
                drum_data = self.karplus_strong_drum(drum_wavetable, self.drum_and_guitar_sampleRate, 1.0)
            else:
                drum_data = self.karplus_strong_drum(drum_wavetable, self.drum_and_guitar_sampleRate, 0.3)

            sd.play(drum_data, self.drum_and_guitar_sampleRate)


        elif self.ui.mw.sender().objectName() in self.guitar_strings:
            String = GuitarString(self.freqs[self.guitar_strings.index(self.ui.mw.sender().objectName())],
                                  self.delays[self.guitar_strings.index(self.ui.mw.sender().objectName())],
                                  self.drum_and_guitar_sampleRate,
                                  self.stretch_factors[self.guitar_strings.index(self.ui.mw.sender().objectName())])

            guitar_sound = [String.get_sample() for sample in range(self.drum_and_guitar_sampleRate)]
            guitar_norm = guitar_sound / max(guitar_sound)
            guitar_sound = self.guitar_volume * guitar_norm

            sd.play(guitar_sound, self.drum_and_guitar_sampleRate)

    def connect_sliders(self, slider_index):
        self.slider_arr[slider_index].sliderReleased.connect(lambda: self.slidervalue(slider_index))

    def slidervalue(self, slider_index):
        self.value = self.slider_arr[slider_index].value()
        self.modify_signal(slider_index, self.value)
        logging.debug('slider number {} has changed its value to {}'.format(slider_index, self.value))

    def Reset_slider_gain(self):
        for i in range(len(self.slider_arr)):
            self.slider_arr[i].setValue(1)
            self.gains[i] = 1.0

    def load(self):
        self.ui.SignalView.clear()
        self.Reset_slider_gain()
        self.filename, self.format = QtWidgets.QFileDialog.getOpenFileName(None, "Load Signal File", "")
        self.filename = self.filename.split('/')[-1]
        self.format = self.filename.split('.')[-1]
        logging.debug('file name is {}'.format(self.filename))
        logging.debug('file format is {}'.format(self.format))

        if self.filename == "":
            pass
        else:
            if self.format != "wav":
                self.show_popup("Not a .wav file", 'Please upload a .wav file')
            else:
                self.samplerate, self.song_data = read(self.filename)
                logging.debug('samplerate is {}'.format(self.samplerate))
                logging.debug('song data length is {}'.format(len(self.song_data)))
                # self.song_data = [i for i in self.song_data if i != 0]
                self.duration = len(self.song_data) / self.samplerate
                self.time = np.arange(0, self.duration, 1 / self.samplerate)  # time vector
                self.zeros = np.zeros(self.song_data.size)  # when volume equal zero play an array of zeros
                self.convert_to_fft()
                self.Normalize_and_setVolume()
                self.ui.SignalView.plot(self.time, self.song_data)
                self.step = 0

    def convert_to_fft(self):
        self.original_signal_fft = np.fft.rfft(self.song_data)
        self.modified_fft = np.copy(self.original_signal_fft)  # this is the copy to operate on and update
        self.fft_fre = np.fft.rfftfreq(n=len(self.song_data),
                                       d=1 / self.samplerate)  # gets the sample frequency bins per cycle
        self.freq_bins = int(len(self.song_data) * 0.5)  # to stop the mirroring
        self.update_plots(self.original_signal_fft)

    def convert_ifft(self, frequency_controld_sig):
        self.song_data = np.fft.irfft(frequency_controld_sig)
        # self.song_data = self.song_data.real
        self.ui.SignalView.clear()
        self.song_data = np.array(self.song_data, dtype=np.int32)  # need to convert to numpy array
        self.Normalize_and_setVolume()
        self.checkPlaying()
        self.update_starter_point_and_plot(self.bol_play)
        self.ui.SignalView.plot(self.time, self.song_data)

    def checkPlaying(self):
        self.bol_play = True
        self.check_play_pause()

    def update_plots(self, frequency_controled_signal):
        self.ui.axes.clear()
        self.ui.axes1.clear()
        self.ui.axes.set_xlabel('Time')
        self.ui.axes.set_ylabel('Frequency')
        self.ui.axes1.set_xlabel('Frequency')
        self.ui.axes1.set_ylabel('Spectral Power')
        # negative freq is the cuz of mathimatical results, complex component that is rotation
        self.ui.axes.specgram(self.song_data, Fs=self.samplerate, cmap=mpl.cm.cool)
        self.ui.figure.colorbar(mpl.cm.ScalarMappable(norm=self.ui.norm, cmap=mpl.cm.cool),
                                cax=self.ui.c_bar_ax, orientation='vertical')
        # spec_power = np.abs(frequency_controled_signal) / len(frequency_controled_signal) # normalized spectral power
        spec_power = np.abs(frequency_controled_signal) / frequency_controled_signal.max()  # normalized spectral power
        self.ui.axes1.plot(self.fft_fre,
                                         spec_power)  # reads the first half only to avoid mirroring
        self.ui.canvas.draw()

    def frequency_control(self, min_freq, max_freq, level, gain):
        self.modified_fft[(self.fft_fre >= min_freq) & (self.fft_fre <= max_freq)] = \
            self.modified_fft[(self.fft_fre >= min_freq) & (self.fft_fre <= max_freq)] / self.gains[level]
        self.gains[level] = gain
        self.modified_fft[(self.fft_fre >= min_freq) & (self.fft_fre <= max_freq)] = \
            self.modified_fft[(self.fft_fre >= min_freq) & (self.fft_fre <= max_freq)] * self.gains[level]

        self.update_plots(self.modified_fft)
        self.convert_ifft(self.modified_fft)

    def check_play_pause(self):
        if self.ui.PlayButton.text() == "PLAY":
            self.bol_play = False

    def modify_signal(self, level_idx, gain):
        gain += 0.00001
        self.frequency_control(self.levels_min[level_idx], self.levels_max[level_idx], level=level_idx, gain=gain)

    def start(self):
        if self.step_right == 0:
            self.ui.timer.timeout.connect(self.update_plot_data)
        self.isPaused = False
        self.ui.timer.start(100)

    def update_plot_data(self):

        if not self.isPaused:
            self.step_right = self.step + 2
            self.step += 0.1

            self.ui.SignalView.plotItem.setXRange(self.step, self.step_right)
            if int(self.step) == int(self.time[-1]):
                self.ui.timer.stop()

    def update_starter_point_and_plot(self, bol_check):
        if bol_check == False:
            self.bol_play = False
        self.x_mid = (self.step + self.step_right) / 2
        self.starter_point = (self.x_mid / self.duration) * len(self.song_data)
        if (self.bol_play):
            sd.play(self.song_data[int(self.starter_point):], self.samplerate)

    def play(self):

        self.update_starter_point_and_plot(False)
        if self.ui.PlayButton.text() == "PLAY":
            self.start()
            self.Normalize_and_setVolume()
            sd.play(self.song_data[int(self.starter_point):], self.samplerate)
            self.ui.PlayButton.setText("STOP")
        else:
            self.isPaused = True
            sd.stop()  # should be the pause i think
            self.ui.PlayButton.setText("PLAY")

    def Set_Volume(self):
        self.bol_play = True
        self.vol = self.ui.powerbar.getvalue() / 100
        if self.vol == 0:
            sd.play(self.zeros, self.samplerate)
        else:
            logging.info('Volume level is {}'.format(self.ui.powerbar.getvalue()))
            self.Normalize_and_setVolume()
            self.check_play_pause()
            self.update_starter_point_and_plot(self.bol_play)
            # sd.play(self.song_data[int(self.starter_point):], self.samplerate)

    def Normalize_and_setVolume(self):
        data_norm = self.song_data / self.song_data.max()
        self.song_data = self.vol * data_norm

    def show_popup(self, message, information):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText(information)
        msg.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
