# website: Course Approval Request Forms

## Things you'll need

* python3
* pip3
* yarn or npm
* Flow
* node

You can get most of these with [Homebrew](https://brew.sh/) on mac.

## Versions

* Python 3.6.5
* pip 10.0.1
* yarn 1.6.0
* node 9.11.1

## Setup

    python3 -m venv env
    source env/bin/activate

Verify you are now in a Python3 environment:

    python --version

Hopefully you're at or ahead of 3.6.5
Now we'll install the packages from the setup egg:

    pip3 install -e .

Alternatively, if that gives you trouble or you would prefer to have an exact clone of my development environment, you can use the `requirements.txt`

    pip3 install -r requirements.txt

Notice the Sass manifest located in `setup.py`
This precompiles all of the Sass .scss files into old school css files in `/static/css`
More on this can be found [here](https://sass.github.io/libsass-python/frameworks/flask.html).

Install the Javascript packages:

    yarn

Set the environment:

    . setdev

Run the server:

    flask run

Alternatively, for a more configurable setup:

    python3 run.py

Open a new session in your terminal in the same working directory and run this:

    sudo yarn run watch

This command starts webpacker and will "watch" your .jsx files, meaning it will recompile when you make changes and hit save. It's a huge time-saver.

Check out the app running on localhost:5000 This port can be configured by using `run.py`

## References

* [BlueprintJS](http://blueprintjs.com/docs/v2/#blueprint) for the front-end
* [WTForms](https://media.readthedocs.org/pdf/wtforms/2.1/wtforms.pdf) for form validation

<FileInput
fill
large
text={"Upload " + this.state.selected.slice(0, -1) + " Image..."}
onInputChange={ev => console.log(ev)}
/>
