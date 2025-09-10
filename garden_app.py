# Determine advice based on the season
# Store the advice inside a varible this will make things easier to use
# dictonaries
def season_advice(season):
    if season == "summer":
        advice = "Water your plants regularly and provide some shade."
        print("Suggested: Pentas")
        return advice
    elif season == "winter":
        advice = "Protect your plants from frost with covers."
        print("Suggested: Pansies")
        return advice
    elif season == "spring":
        advice = (
            "Choosing the right plants for your conditions, "
            "and watering deeply and less frequently."
        )
        print("Suggested: Tulips")
        return advice
    elif season == "autumn":
        advice = (
            "Focus on adjusting watering schedules, "
            "providing adequate sunlight, "
            "and protecting plants from frost."
        )
        print("Suggested: Daisy")
        return advice
    else:
        advice = "No advice for this season."


# Determine advice based on the plant type
# Store the advice in a varible so we don't call upon the whole sentence but
# just the varible name
def plant_advice(plant_type):
    if plant_type == "flower":
        advice = "Use fertiliser to encourage blooms."
        return advice
    elif plant_type == "vegetable":
        advice = "Keep an eye out for pests!"
        return advice
    elif plant_type == "herbs":
        advice = (
            "Providing the right amount of sun, water, "
            "and soil conditions."
        )
        return advice
    elif plant_type == "trees":
        advice = "Focus on proper planting, watering, mulching, and pruning."
        return advice
    elif plant_type == "climbers":
        advice = (
            "Ensure proper support, planting location, "
            "and soil conditions."
        )
        return advice
    else:
        advice = "No advice for this type of plant."


# Print the generated advice
def main():
    print(
          "Summer" + "\n"
          "Winter" + "\n"
          "Spring" + "\n"
          "Autumn"
        )
    season = input("Enter the season: ")
    print(
        "\n"
        "Flowers" + "\n"
        "Vegetable" + "\n"
        "Herbs" + "\n"
        "Trees" + "\n"
        "Climbers"
        )
    plant_type = input("Enter the plant type: ")

    # Save the messages in a varible
    season_message = season_advice(season)
    plant_message = plant_advice(plant_type)

    # Clean formatted output
    print("\nGardening Advice")
    print(f"Season Advice: {season_message}")
    print(f"Plant Advice: {plant_message}")


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
