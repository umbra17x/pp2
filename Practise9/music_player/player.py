import os
import pygame


class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_playlist()
        self.current_index = 0

        self.is_playing = False
        self.is_stopped = True

    def load_playlist(self):
        tracks = []

        if not os.path.exists(self.music_folder):
            return tracks

        for file_name in os.listdir(self.music_folder):
            if file_name.lower().endswith((".mp3", ".wav")):
                full_path = os.path.join(self.music_folder, file_name)
                tracks.append(full_path)

        tracks.sort()
        return tracks

    def get_current_track_path(self):
        if not self.playlist:
            return None
        return self.playlist[self.current_index]

    def get_current_track_name(self):
        track_path = self.get_current_track_path()
        if track_path is None:
            return "No tracks found"
        return os.path.basename(track_path)

    def play(self):
        if not self.playlist:
            return

        track_path = self.get_current_track_path()
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()

        self.is_playing = True
        self.is_stopped = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_stopped = True

    def next_track(self):
        if not self.playlist:
            return

        self.current_index += 1
        if self.current_index >= len(self.playlist):
            self.current_index = 0

        self.play()

    def previous_track(self):
        if not self.playlist:
            return

        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.playlist) - 1

        self.play()

    def check_auto_next(self):
        if self.is_playing and not pygame.mixer.music.get_busy():
            self.next_track()

    def get_progress_seconds(self):
        """
        Returns playback position in seconds.
        pygame.mixer.music.get_pos() returns milliseconds from start of playback.
        If stopped, it may return -1.
        """
        pos_ms = pygame.mixer.music.get_pos()

        if pos_ms < 0:
            return 0

        return pos_ms // 1000

    def get_playlist_info(self):
        if not self.playlist:
            return []

        result = []
        for i, track in enumerate(self.playlist):
            name = os.path.basename(track)
            if i == self.current_index:
                result.append("> " + name)
            else:
                result.append("  " + name)
        return result