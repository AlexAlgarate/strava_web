from typing import List

import reflex as rx

from strava_web.src.strava_api.get_activities_process.filter_activities import (
    ActivityFilter,
)
from strava_web.utils.config import (
    elevation_column,
    id_activity_column,
    meters_elevation_gain,
    sports_column,
    sports_to_correct,
)

access_token = "Esto es un access token de prueba"


# class Strava(rx.State):
#     display_access_token: str = ""

#     def get_ids(self) -> List[int]:
#         activities = ActivityFilter().filter_activities(
#             columns_sport=sports_column,
#             sports=sports_to_correct,
#             elevation_column=elevation_column,
#             meters_elevation=meters_elevation_gain,
#             id_actvity=id_activity_column,
#         )
#         print(activities)

#     def print_access_token(self):
#         self.display_access_token = access_token


# class PrintSomething(rx.State):
#     text_to_print: str = ""

#     def print_text(self, text: str):
#         self.text_to_print = text


# button_style = {
#     "border": "0.1em solid",
#     "padding": "0.5em",
#     "border_radius": "0.5em",
#     "_hover": {
#         "color": rx.color_mode_cond(
#             light="rgb(107,99,246)",
#             dark="rgb(179, 175, 255)",
#         )
#     },
# }


# def index() -> rx.Component:
#     return rx.fragment(
#         rx.color_mode_button(rx.color_mode_icon(), float="right"),
#         rx.vstack(
#             rx.heading("Welcome to Cejoland!", font_size="3em"),
#             # rx.link(
#             #     rx.button(
#             #         "Get your fucking Strava activity id's",
#             #         on_click=Strava.get_ids,
#             #     ),
#             #     style=button_style,
#             # ),
#             # rx.vstack(
#             #     rx.button(
#             #         "Print access token",
#             #         style=button_style,
#             #         on_click=Strava.print_access_token,
#             #     ),
#             #     rx.cond(
#             #         Strava.display_access_token != "",
#             #         rx.text(Strava.display_access_token),
#             #         None,
#             #     ),
#             # ),
#             rx.vstack(
#                 rx.button(
#                     "Print text",
#                     style=button_style,
#                     on_click=PrintSomething.print_text(text="hola mundo"),
#                 ),
#                 rx.cond(
#                     Strava.display_access_token != "",
#                     rx.text(Strava.display_access_token),
#                     None,
#                 ),
#             ),
#             spacing="1.5em",
#             font_size="2em",
#             padding_top="10%",
#         ),
#     )


class TokenState(rx.State):
    input_text: str = ""
    output_text: str = ""

    def get_strava_token(self):
        self.output_text = self.input_text


def index():
    return rx.vstack(
        rx.input(
            value=TokenState.input_text,
            on_change=TokenState.set_input_text,
        ),
        rx.button(
            "Get Token",
            on_click=TokenState.get_strava_token,
        ),
        rx.text(TokenState.output_text),
    )


app = rx.App()
app.add_page(index)
