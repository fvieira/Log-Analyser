#! /usr/bin/env python
import subprocess
import argparse

COLORS = ['31', '32', '33', '34', '35', '36', '37']


def main():
    parser = argparse.ArgumentParser(description='Log analyser.')
    parser.add_argument('filename', help='Path to the log file to analyse.')
    parser.add_argument('regexes', help='Regexes to apply to each log line.', nargs='+')
    args = parser.parse_args()

    if len(args.regexes) > len(COLORS):
        print('Too many regexes. Only {0} colors are supported.'.format(len(COLORS)))
    else:
        awk_param_parts = []
        for i, regex in enumerate(args.regexes):
            awk_param_parts.append('/{0}/ {{print "\033[{1}m" $0 "\033[39m"}}'.format(regex, COLORS[i]))
        awk_param = "'{0}'".format(' '.join(awk_param_parts))
        cmd = 'cat {0} | awk {1} | less -R'.format(args.filename, awk_param)
        print(subprocess.check_output(cmd, shell=True))


if __name__ == '__main__':
    main()
