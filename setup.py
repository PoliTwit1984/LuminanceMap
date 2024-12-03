print("""
To create a right-click action for the luminance map script:

1. Open Automator (from Applications or Spotlight)
2. Choose "New Document"
3. Select "Quick Action" (or "Service" in older macOS versions)
4. Configure the workflow settings at the top:
   - Workflow receives current: "image files"
   - in: "any application"

5. Add a "Run Shell Script" action (search for it in the actions library)
6. Set "Shell" to "/bin/bash"
7. Set "Pass input" to "as arguments"
8. Enter this command (replace the path with your actual script location):

   /Users/joewilson/PythonProjects/LuminanceMap/create_luminance_map.sh "$@"

9. Save the workflow with a name like "Create Luminance Map"

Now you can right-click any image file and select:
Services > Create Luminance Map (or Quick Actions > Create Luminance Map)

The processed image will be saved in the same directory as the original with 'processed_' prefix.

Note: If you move the LuminanceMap folder, you'll need to update the path in the Automator workflow.
""")
