# Remove text color on .tex files

## Description
When submitting scientific papers for revision, it is common for journals to request corrections to be highlighted in red text. However, before submitting the final version, it is necessary to remove the red text color commands. This simple script eliminates the need to manually remove these commands, saving you time and effort.

## Usage
- Run the executable file (.exe).
- Enter the file path of the .tex file when prompted.
- The script will create a new folder in the same location as the original file, containing the modified version without the red text color commands.

Command to be removed from the .tex file:

```bash
\textcolor{red}{...}
```

## Updates
- Includes the possibility of having nested commands inside of the textcolor command. Like:

```bash
\textcolor{red}{... \textit{...} ...}
```

Minor bugs still might be present. Feel free to contribute to the project or provide feedback. 