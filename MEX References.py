# MEX Reference Generator for External Material
# Author: Miska Rihu
# Modified: 03.04.2022
# Version: R1
###############################################################################

DATE_DELIMN = "-"
TAB = 4 * " "
SPACER = 80 * "="

ERR_MALFORMED_DATE = "    Error: Parsing date failed due to malformed input string."

class REFERENCE:
    author = ""
    title = ""
    publisher = ""
    publication = ""
    howpublished = ""
    url = ""
    publication_date = ""
    reference_date = ""
    translator = ""
    modified_by = ""
    note = ""
    

def generatePreview(ref):
    preview = ""
    if (ref.author != ""):
        preview += "Lähde: {0}. ".format(ref.author)
        
    if (ref.title != ""):
        preview += "{0}. ".format(ref.title)
        
    if (ref.publisher != ""):
        preview += "{0}. ".format(ref.publisher)
        
    if (ref.publication != ""):
        preview += "{0}. ".format(ref.publication)
        
    if (ref.howpublished != ""):
        preview += "{0}. ".format(ref.howpublished)
        
    if (ref.url != ""):
        preview += "{0}. ".format(ref.url)
        
    if (ref.publication_date != ""):
        preview += "Julkaistu: {0}.{1}.{2}. ".format(ref.publication_date[2], ref.publication_date[1], ref.publication_date[0])
        
    if (ref.reference_date != ""):
        preview += "Julkaistu: {0}.{1}.{2}. ".format(ref.reference_date[2], ref.reference_date[1], ref.reference_date[0])
        
    if (ref.translator != ""):
        preview += "Käännös: {0}. ".format(ref.translator)
        
    if (ref.modified_by != ""):
        preview += "Muokkaus: {0}. ".format(ref.modified_by)
        
    if (ref.note != ""):
        preview += "{0}".format(ref.note)
    
    return preview


def generateCode(ref):
    code = 5 * TAB + "<e:reference>\n"

    if (ref.author != ""):
        code += 6 * TAB + "<e:author>{0}<e/e:author>\n".format(ref.author)

    if (ref.title != ""):
        code += 6 * TAB + "<e:title>{0}<e/e:title>\n".format(ref.title)

    if (ref.publisher != ""):
        code += 6 * TAB + "<e:publisher>{0}<e/e:publisher>\n".format(ref.publisher)

    if (ref.publication != ""):
        code += 6 * TAB + "<e:publication>{0}<e/e:publication>\n".format(ref.publication)

    if (ref.howpublished != ""):
        code += 6 * TAB + "<e:howpublished>{0}<e/e:howpublished>\n".format(ref.howpublished)

    if (ref.url != ""):
        code += 6 * TAB + "<e:url>{0}<e/e:url>\n".format(ref.url)

    if (ref.publication_date != ""):
        code += 6 * TAB + "<e:publication-date>{0}-{1}-{2}<e/e:publication-date>\n".format(ref.publication_date[0], ref.publication_date[1], ref.publication_date[2])

    if (ref.reference_date != ""):
        code += 6 * TAB + "<e:reference-date>{0}-{1}-{2}<e/e:reference-date>\n".format(ref.reference_date[0], ref.reference_date[1], ref.reference_date[2])

    if (ref.translator != ""):
        code += 6 * TAB + "<e:translator>{0}<e/e:translator>\n".format(ref.translator)

    if (ref.modified_by != ""):
        code += 6 * TAB + "<e:modified-by>{0}<e/e:modified-by>\n".format(ref.modified_by)

    if (ref.note != ""):
        code += 6 * TAB + "<e:note>{0}<e/e:note>\n".format(ref.note)

    code += 5 * TAB + "</e:reference>"
    
    return code


def main():
    print("MEX Reference Generator for External Material")
    print(SPACER)
    print()
    
    while (True):
        print("Uusi lähdeviittaus")
        print("Minkä tahansa kohdan voi jättää tyhjäksi. Tällöin sitä ei lisätä viittaukseen.")
        print(SPACER)
        ref = REFERENCE()
        ref.author = input("Lähde (esim. Matti Mallikas tai Wikipedia): ")
        ref.title = input("Otsikko: ")
        ref.publisher = input("Julkaisija: ")
        ref.publication = input("publication: ")
        ref.howpublished = input("Julkaisumuoto (esim. YouTube): ")
        ref.url = input("URL: ")
        
        date = ""
        date = input("Julkaistu (pvm. muodossa vvvv-kk-pp): ")
        if (date != ""):
            try:
                date = date.split(DATE_DELIMN)
                for i in date:
                    i = int(i)
                ref.publication_date = date
            except Exception:
                print(ERR_MALFORMED_DATE)
              
        date = ""
        date = input("Viitattu (pvm. muodossa vvvv-kk-pp): ")
        if (date != ""):
            try:
                date = date.split(DATE_DELIMN)
                for i in date:
                    i = int(i)
                ref.reference_date = date
            except Exception:
                print(ERR_MALFORMED_DATE)
            
        ref.translator = input("Kääntäjä: ")
        ref.modified_by = input("Muokkaaja (esim. oma nimesi, jos olet muokannut lähdemateriaalia: ")
        ref.note = input("Huomiota: ")

        preview = generatePreview(ref)
        code = generateCode(ref)

        print(SPACER)
        print("Preview:")
        print("--------")
        print(preview)
        
        print(SPACER)
        print("Paste the following code inside <e:external-material></e:external-material>")
        print()
        print("Code:")
        print("-----")
        print(code)
        print(SPACER)
        print()


main()
