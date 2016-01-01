import fileinput
import re
from warnings import warn

def remove_eqrefs(filepath):
    '''
    In a LaTeX document with labelled equations, remove 
    the internal links and replace all eqrefs with just
    the appropriate numbers. This is necessary when
    converting the document to another file format or when
    submitting the TeX file to a journal
    
    Parameters
    ----------
    
    filepath : str
        Path to the LaTeX file. This will be overridden

    Examples
    --------

    >>>remove_eqrefs('documents/myfile.tex')
    
    '''
    
    f = open(filepath,'r')
    txt = f.read()

    all_labelled_eqs = re.findall(r'\\begin{equation}((.|\n)*?)\\label((.|\n)*?)\\end{equation}',txt)
    all_eqs = re.findall(r'\\begin{equation}((.|\n)*?)\\end{equation}',txt)

    all_labelled_aligns = re.findall(r'\\begin{align}((.|\n)*?)\\label((.|\n)*?)\\end{align}',txt)
    all_aligns = re.findall(r'\\begin{align}((.|\n)*?)\\end{align}',txt)
    
    if len(all_labelled_eqs) < len(all_eqs):
        warnings.warn('There are some unlabelled (but numbered) equations that will throw off the\
                      automatic numbering system')
    if len(all_labelled_aligns) < len(all_aligns):
        warnings.warn('There are some unlabelled (but numbered) equations that will throw off the\
                      automatic numbering system')
        

    my_file = fileinput.FileInput(filepath)
    all_labels = []
    for line in my_file:
        matches = re.findall('label{.*}',line)
        if matches:
            all_labels.append(matches[0][6:-1])

    for ind, label in enumerate(all_labels):
        with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace('\eqref{' + label + '}', 'Eq. ' + str(ind+1)), end='')
