#!/usr/bin/env python
"""
Creates a technology radar based on the input from a csv file using a HTML template

format of the CSV as follows:

name,ring,quadrant,moved,link were:

* Name =
* ring =
* Quadrant =
* moved  =
* Link =



Exameple:
Java,INNER,Bottom Right,none,../docs/java.html

Based on zalando's technology radar

Requires:
jinja2 for templates


"""
# CSV file reading utilities
import csv

# HTML template framework
import jinja2


#common vars, edit here for convenience
data_file = 'data.csv'
template_file = 'tech_radar_templates.html'
output_file = 'radar.html'


#please note, we're going cowboy here, no error management ahead, use at your own risk :)
def main():

    loader = jinja2.FileSystemLoader('./')
    jinjaEnv = jinja2.Environment(loader=loader)
    template = jinjaEnv.get_template(template_file)

    #import data.csv file
    with open(data_file) as cvsfile:
        reader = csv.DictReader (cvsfile, delimiter=',')
        output = template.render(entries = reader)
        #writing the file
        with open(output_file, 'w') as f:
            f.write ( output )
            f.close()

#main
if __name__ == "__main__":
    main()
