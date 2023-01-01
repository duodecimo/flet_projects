import flet as ft
import vlc
import time


def main(page: ft.Page):
    page.title = "3Minds Video player"

    def on_dialog_result(e: ft.FilePickerResultEvent):
        selected = e.files[0].path
        source.value = selected
        page.update()

    input = ft.Text(value="input", weight="bold", size=24)
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
    page.update()
    btn_file_picker = ft.ElevatedButton(
        text="choose file ...",
        on_click=lambda _: file_picker.pick_files(allow_multiple=False),
    )

    def play_movie(e):
        # creating vlc media player object
        media_player = vlc.MediaPlayer()

        # media object
        media = vlc.Media(source.value)

        # setting media to the media player
        media_player.set_media(media)

        # start playing video
        media_player.play()

        # wait so the video can be played for 5 seconds
        # irrespective for length of video
        time.sleep(5)
        # getting subtitle description
        subtitle = media_player.video_get_spu_description()

        # printing subtitle description
        print("Subtitle Description")
        print(subtitle)

    output = ft.Text(value="output", weight="bold", size=24)
    btn_play = ft.ElevatedButton(
        text="play",
        on_click=play_movie,
    )
    source = ft.Text(value="", style="bodySmall")
    page.add(
        ft.Row(
            [input],
        ),
        ft.Row(
            [btn_file_picker],
        ),
        ft.Row(
            [source],
        ),
        ft.Row(
            [
                output,
            ],
        ),
        ft.Row(
            [btn_play],
        ),
    )


ft.app(target=main)
