from pathlib import Path
import re
import base64

dir = Path(__file__).parents[1]


def convert():
    re_img = re.compile('<img src=(.*\.png)')
    for file in Path(".").glob("**/*.ipynb"):
        file = Path(file).resolve()
        print(f'{file}')

        def repl_img(match):
            p = (file.parent / match.group(1)).resolve()
            print(f"Convert image {p}\n")
            if p.is_file():
                with open(p, "rb") as f:
                    s = base64.b64encode(f.read()).decode('ascii')
                    return f'<img src="data:image/png;base64,{s}"'

        with open(file, "r") as f:
            output = re_img.sub(repl_img, f.read())
        with open(file, "w") as f:
            f.write(output)


convert()
