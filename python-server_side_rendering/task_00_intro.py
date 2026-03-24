#!/usr/bin/python3
"""Module for generating invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template.

    Args:
        template (str): Template string with placeholders.
        attendees (list): List of dictionaries with attendee data.

    Returns:
        None
    """
    placeholders = ["name", "event_title", "event_date", "event_location"]

    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        with open(filename, "w", encoding="utf-8") as out_file:
            out_file.write(output)
