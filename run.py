import pyfiglet, time, sys,argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", dest="text", help="Enter The Text You Want to Format")
    arguments = parser.parse_args()
    return arguments.text



def format_as_lines(text):

    LineText=text.split()

    for texts in LineText:
        sys.stdout.write(pyfiglet.figlet_format(texts, justify="center", font="standard", width=100))
        sys.stdout.flush()
        time.sleep(0.3)



def format_as_one_line(text):
    
    sys.stdout.write(pyfiglet.figlet_format(text, justify="center",font="standard",width=100))
    sys.stdout.flush()
    time.sleep(0.5)

text = get_arguments()
format_as_lines(text)
