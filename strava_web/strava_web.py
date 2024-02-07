from typing import List

import reflex as rx

from rxconfig import config
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

docs_url = "https://github.com/AlexAlgarate/wedding_web/"
filename = f"{config.app_name}/{config.app_name}.py"


class GetIDStrava(rx.State):

    def get_ids(self) -> List[int]:
        activities = ActivityFilter().filter_activities(
            columns_sport=sports_column,
            sports=sports_to_correct,
            elevation_column=elevation_column,
            meters_elevation=meters_elevation_gain,
            id_actvity=id_activity_column,
        )
        print(activities)


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to Cejoland!", font_size="3em"),
            rx.link(
                rx.button(
                    "Get your fucking Strava activity id's",
                    on_click=GetIDStrava.get_ids,
                ),
                # href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Create app instance and add index page.
app = rx.App()
app.add_page(index)
