## Script (Python) "evilchecking"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Evil Checking

stool = context.portal_skins
skin_folders = stool.objectIds()
# loop through all the skins dirs
for folder in skin_folders:
    folder = stool[folder]
    # only return true if it's not a fs dir and has something in it
    if folder.meta_type != 'Filesystem Directory View' and folder.objectIds():
        return True
return False
