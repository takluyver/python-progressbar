'''Text progress bar library for Python.

A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets. A widget is an object that may display
differently depending on the state of the progress bar. There are three types
of widgets:

 - a string, which always shows itself

 - a ProgressBarWidget, which may return a different value every time its
   update method is called

 - a ProgressBarWidgetHFill, which is like ProgressBarWidget, except it
   expands to fill the remaining width of the line.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.
'''

import datetime

__package_name__ = 'progressbar2'
__author__ = 'Rick van Hattem'
__author_email__ = 'Wolph@Wol.ph'
__url__ = 'https://github.com/WoLpH/python-progressbar'
__date__ = str(datetime.date.today())
__version__ = '3.0.1'
