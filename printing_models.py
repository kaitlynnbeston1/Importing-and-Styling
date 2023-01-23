import printingFunctions
unprinted = ["phone case", "robot pendant", "dodecahedron"]
complete = []
printingFunctions.print_models(unprinted, complete)
printingFunctions.show_completed_models(complete)

unprinted.append("Computer keycaps")
unprinted.append("action figure")
unprinted.append("fake lightsaber")
unprinted.append("SSD casing")

printingFunctions.print_models(unprinted, complete)
printingFunctions.show_completed_models(complete)
