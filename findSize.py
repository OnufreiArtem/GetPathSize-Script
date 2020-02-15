import os
import optparse

def get_size(start_path = '.'):
    print('Getting size of "{0}" ...'.format(start_path))
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size




def Main():
  parser = optparse.OptionParser('user %prog -p <string-path>')
  parser.add_option('-p', '--path', type='string', dest='path', help='specify path')

  data = parser.parse_args()
  options = data[0]

  if options.path == None:
    print(parser.usage)
    exit(0)
  else:
      try:
        bytes = get_size(options.path)
        kilobytes = int(bytes / 1024)
        megabytes = int(kilobytes / 1024)
        gigabytes = int(megabytes / 1024)
        print("\n{3} GB {2} MB {1} KB {0} B\n".format(bytes, kilobytes, megabytes, gigabytes))

      except:
          print('Error: Probably wrong path. Try again...')

if __name__ == "__main__":
  Main()