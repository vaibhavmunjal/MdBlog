# MdBlog
A Mark Down style blog


To run the app download modules specified in requirements.txt

#### Add the app in the installed modules
 <!-- app module -->
`'blog.apps.BlogConfig',`

<!-- Third party modules -->
`'bootstrap4',`

`'pagedown',`

`'markdown_deux',`

`'crispy_forms',`

### Settings.py
#### set the media and static path
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

#### set style module format
CRISPY_TEMPLATE_PACK = 'bootstrap4'
