import time
import pyxel
from game.config import Config
from sheet.reader.sheet_reader import SheetReader
from game.playthrough.manager_actions import ManagerActions
from game.constants import Constants
from game.frames import Frames
from game.playthrough.effect.effect_controller import EffectController
from game.playthrough.note import PositionedNote
import game.playthrough.criteria_manager as criteria_manager
import util as util
from pyglet import media
import logger


class Counter:
    def __init__(self):
        self.misses = 0
        self.bads = 0
        self.greats = 0
        self.perfects = 0

    def get_prop(self):
        return {
            "Perfect": self.perfects,
            "Great": self.greats,
            "Bad": self.bads,
            "Miss": self.misses
        }

    def get_total_notes(self):
        return self.misses + self.bads + self.greats + self.perfects

    def get_tp(self):
        total_notes = self.get_total_notes()
        weight_count = self.misses * 0 + self.bads * 1 + self.greats * 2 + self.perfects * 3
        avg_weight = weight_count / total_notes
        tp = avg_weight / 0.03
        return tp

    def get_avg_acc(self):
        total_notes = self.get_total_notes()
        weight_count = self.misses * Constants.TOLERANCE[0] + self.bads * Constants.TOLERANCE[1] + self.greats * Constants.TOLERANCE[2] + self.perfects * Constants.TOLERANCE[3]
        avg_weight = weight_count / total_notes
        return avg_weight

    def get_avg_dev(self):
        count_list = [self.misses, self.bads, self.greats, self.perfects]
        tp: float = self.get_avg_acc()
        abs_dev = [abs((Constants.TOLERANCE[n - 1] if n != 0 else 0) - tp) * count_list[n] for n in range(4)]
        avg_dev = sum(abs_dev) / self.get_total_notes()
        return avg_dev


class NoteManager:
    # TODO: make the tp be shown while playing
    # @staticmethod
    # def count(manager):
    #     counter = Counter()
    #     for note in manager.notes:
    #         if not isinstance(note, PositionedNote):
    #             continue
    #         if note.result == Constants.PlayThrough.NoteIndicator.PERFECT:
    #             counter.perfects += 1
    #         elif note.result == Constants.PlayThrough.NoteIndicator.GREAT:
    #             counter.greats += 1
    #         elif note.result == Constants.PlayThrough.NoteIndicator.BAD:
    #             counter.bads += 1
    #         elif note.result == Constants.PlayThrough.NoteIndicator.MISS:
    #             counter.misses += 1
    #     return counter
    def __init__(self, sheet: SheetReader, side_distances: list, music_source: str):
        self.meta: dict = sheet.data
        # logger.print(self.meta)
        self.notes: list = [ManagerActions.from_note(x) for x in sheet.notes]
        # logger.print("\n".join([str(x) for x in self.notes]))
        self.side_distances: list = side_distances
        self.music_source: str = music_source
        self.music: media.Source = media.load(self.music_source)
        self.music_len: float = self.music.duration
        self.music_started: bool = False
        self.started: bool = False
        self.initiate: bool = True
        self.finished: bool = False
        self.paused: bool = False
        self.score: int = 0
        self.combo: int = 0
        self.draw_default_criteria: bool = True
        # Basically, when a note is finished, this is used to draw a rect around it for a frame
        # since there should only be two frames, we dont need to generalise it
        self.res_frames: list = []
        self.res_frames2: list = []

        self.counter: Counter = Counter()
        self.last_indicated_frame_pos = util.grid(
            Constants.Cast.WIDTH, Constants.Cast.HEIGHT,
            16, 16,
            1, 1
        )
        self.score_pos = util.grid(
            Constants.Cast.WIDTH, Constants.Cast.HEIGHT,
            16, 16,
            12, 1
        )
        self.indicator_circle_pos = Constants.Cast.center(
            Frames.PlayThrough.INDICATOR_CIRCLE.width, Frames.PlayThrough.INDICATOR_CIRCLE.height)
        self.perfect_note_score = Constants.PlayThrough.Score.TOTAL_SCORE / (len(self.notes) * Constants.PlayThrough.NoteIndicator.INDICATORS().index(Constants.PlayThrough.NoteIndicator.PERFECT))

    def prepare(self):
        pass

    def start(self):
        self.initiate = True

    def pause(self):
        """
        pauses the music and the sheet

        Bug exists
        """
        if not self.paused:
            pass
            # pygame.mixer.music.pause()
            # self.last_pause_time = time.time()
            # logger.print(
            #     f"Game paused. Total Time: {self.total_time},  Start Time: {self.start_time}")
        else:
            pass
            # pygame.mixer.music.unpause()
            # self.start_time += time.time() - self.last_pause_time
            # logger.print(
            #     f"Game continued. Total Time: {self.total_time}, Start Time: {self.start_time}")
        self.paused = not self.paused

    def update_time(self) -> None:
        if self.music_started:
            self.total_time = (
                self.meta["music_offset"] / 1000 + Config.PLAYER.time)
        else:
            self.total_time = time.time() - self.start_time
        if (not self.music_started) and self.total_time * 1000 >= self.meta["music_offset"]:
            Config.release_player()
            Config.PLAYER = self.music.play()
            Config.PLAYER.loop = False
            self.music_started = True

    @util.timeit(without=(-1, 30))
    # @numba.jit()
    def update(self):
        if self.paused:
            return None
        if self.initiate:
            self.start_time = time.time()
            self.total_time: float = 0
            self.initiate = False
            self.started = True
            self.finished = False
            self.last_indicator = Constants.PlayThrough.NoteIndicator.NOT_IN_BOUND
        self.update_time()
        EffectController.update(total_time=self.total_time * 1000)

        # Test if the default criteria should be drawn

        self.draw_default_criteria = False
        for crit in criteria_manager.criterias:
            if crit is not None and crit[0] == criteria_manager.CenterNote:
                self.draw_default_criteria = True
                break

        if self.music_started and Config.PLAYER.time >= self.music_len:
            logger.print("Finished")
            self.finished = True
            EffectController.clear_effects()
            return None
        res = Constants.PlayThrough.NoteIndicator.NOT_IN_BOUND
        to_be_removed = []
        for note in self.notes:
            res_indicate = note.update(self.total_time * 1000)
            if not isinstance(note, PositionedNote):
                continue
            if res_indicate != Constants.PlayThrough.NoteIndicator.NOT_IN_BOUND:
                res = res_indicate
                if res_indicate in [Constants.PlayThrough.NoteIndicator.BAD, Constants.PlayThrough.NoteIndicator.MISS]:
                    self.combo = 0
                else:
                    self.combo += 1
                if res_indicate != Constants.PlayThrough.NoteIndicator.MISS:
                    self.score += self.perfect_note_score * Constants.PlayThrough.NoteIndicator.INDICATORS().index(res_indicate)
                if res_indicate == Constants.PlayThrough.NoteIndicator.PERFECT:
                    self.counter.perfects += 1
                elif res_indicate == Constants.PlayThrough.NoteIndicator.GREAT:
                    self.counter.greats += 1
                elif res_indicate == Constants.PlayThrough.NoteIndicator.BAD:
                    self.counter.bads += 1
                elif res_indicate == Constants.PlayThrough.NoteIndicator.MISS:
                    self.counter.misses += 1
                to_be_removed.append(note)
        for tbr_element in to_be_removed:
            tbr_element: PositionedNote = tbr_element
            self.res_frames.append([tbr_element.pos, tbr_element.result])
            self.notes.remove(tbr_element)
        if res != Constants.PlayThrough.NoteIndicator.NOT_IN_BOUND:
            self.last_indicator = res
        self.last_indicated_frame = Constants.PlayThrough.NoteIndicator.getFrame(
            self.last_indicator)
    # @util.timeit(within=(40, -1))

    @util.timeit(without=(-1, 30))
    def draw(self):
        # Draw effects first
        EffectController.draw(total_time=self.total_time)

        # Draw criteria if default
        if self.draw_default_criteria:
            Frames.PlayThrough.INDICATOR_CIRCLE.draw(*Constants.Cast.center(32, 32))

        # Draw score
        pyxel.text(*self.score_pos, f"Score: {int(self.score)}", 12)

        pyxel.text(128, 8, f"{self.combo}", 12)

        # Draw last indicator result
        self.last_indicated_frame.draw(*self.last_indicated_frame_pos)

        # Draw note finish frames
        for tbr in self.res_frames:
            pyxel.rectb(tbr[0][0] - 4, tbr[0][1] - 4, 8, 8, 6)
        for tbr in self.res_frames2:
            pyxel.rectb(tbr[0][0] - 4, tbr[0][1] - 4, 8, 8, 6)
        self.res_frames2 = list(self.res_frames)
        self.res_frames.clear()

        # Draw notes
        for note in self.notes:
            note.draw()

        # Draw progress
        if self.music_started:
            progess: int = int((Config.PLAYER.time / self.music_len) * Constants.Cast.WIDTH)
            pyxel.rect(0, 0, progess, 2, 7)
