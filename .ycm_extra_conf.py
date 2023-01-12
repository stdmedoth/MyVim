import os
import ycm_core

flags = [
  '-Wall',
  '-Wextra',
  '-Werror',
  '-Wno-long-long',
  '-Wno-variadic-macros',
  '-fexceptions',
  '-ferror-limit=10000',
  '-DNDEBUG',
  '-std=c99',
  '-xc',
  '-I./',
  '-isystem', '/usr/include',
  '-isystem', '/usr/local/include',

]

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.hpp', '.h'  ]

def FlagsForFile( filename, **kwargs ):
  return {
  'flags': flags,
  'do_cache': True
  }
