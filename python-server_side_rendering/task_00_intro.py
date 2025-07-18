def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error message: template must be string")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error message: attendees must be list and all items in attendees must be dictionary")
        return

    if not template.strip():
        print("Template is empty, no output files generated")
        return

    if not attendees:
        print("No data provided, no output files generated")
        return

    for index, attendee in enumerate(attendees, start=1):
        filled_template = template
        filled_template = filled_template.replace("{name}", attendee.get("name", "N/A"))
        filled_template = filled_template.replace("{event_title}", attendee.get("event_title", "N/A"))
        filled_template = filled_template.replace("{event_date}", attendee.get("event_date", "N/A"))
        filled_template = filled_template.replace("{event_location}", attendee.get("event_location", "N/A"))

        file_name = f"output_{index}.txt"
        try:
            with open(file_name, 'w') as f:
                f.write(filled_template)
            print(f"Generated: {file_name}")
        except Exception as e:
            print(f"Failed to write {file_name}: {e}")
