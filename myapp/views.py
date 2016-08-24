# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render_to_response
from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.encoding import smart_text
from myapp.models import Document
from myapp.models import Msg
from myapp.forms import DocumentForm
from myapp.forms import MsgForm
from django.core.files import File
from .ecc import *

from django.contrib.auth.models import User
from registration.models import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def msg(request):
            # testmsg = encrypt(b'This is a very secret message\n', b'8W;>i^H0qi|J&$coR5MFpR*Vn')
            # testmsg = byte_string.decode(encoding)
            # unicode_text = byte_string.decode(encoding)
            # testmsg1 = smart_text(testmsg, encoding='utf-8', strings_only=True, errors='strict')
            # str2 = bytes("hello world", encoding="UTF-8")
    user = request.user.username
    user = user.encode('utf-8')
    testmsg1 = passphrase_to_pubkey(user)
    return render(request, 'myapp/msg.html', {'testmsg1':testmsg1})


def handle_uploaded_file(f, filename):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def liss(request):
    # Handle file upload

    # MEDIA_FILE = os.path.join(BASE_DIR, 'media/documents/%s.jpg' % os.urandom(10).encode('hex'))

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['docfile'], MEDIA_FILE)
            current_user = request.user
            newdoc = Document(docfile=request.FILES['docfile'], uploader=current_user.id)
            newdoc.save()
            # os.remove(MEDIA_FILE)
            # a.save()
            # encrypt_file(request.FILES['docfile'], MEDIA_FILE, '8W;>i^H0qi|J&$coR5MFpR*Vn')
            # uploaderObj =
            # with open(MEDIA_FILE, 'rw') as f:
            #     mile = File(f)
            #     current_user = request.user
            #     newdoc = Document(docfile=mile, uploader=current_user.id)
            #     newdoc.save()
            #     f.close()




            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('liss'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    """
   return render_to_response(
        'list.html',
        {'documents': documents, 'form': form },
        context_instance=RequestContext(request)
    )
    """
    return render(request,
        'myapp/list.html',
        {'documents': documents, 'form': form }
    )

def encc(request):
    if request.method == 'POST' and (request.POST.get('encrypt')=="Encrypt"):
        # form = DocumentForm(request.POST, request.FILES)
        # if form.is_valid():

        FILENAME0 =request.POST.get('filename')
        # FILENAME1 =FILENAME0[:-12]
        # FILENAME1 =FILENAME1[-20:]
        # user = request.user.username
        # user = user.encode('utf-8')
        testmsg1 = request.POST.get('publickey')

        FILENAME0 =FILENAME0[17:]
        #ENCRYPTFILENAME1 = FILENAME0[:-4]
        ENCRYPTFILENAME1 = FILENAME0

        # FILE0 = os.path.join(BASE_DIR, 'media/documents/%s' % TEMPFILENAME1)
        FILE0 = os.path.join(BASE_DIR, 'media/documents/%s' % FILENAME0)

        # FILENAME = os.path.join(BASE_DIR, 'media/documents/%s.enc' % os.urandom(10).encode('hex'))
        FILENAME = os.path.join(BASE_DIR, 'media/documentstemp/%s.enc' % ENCRYPTFILENAME1)
        #FILENAME = os.path.join(BASE_DIR, 'media/documents/%s.enc' % FILENAME1)
        #newdoc = Document(docfile=request.FILES['docfile'])
        #encrypt_file(open(FILE0,'rw'), FILENAME, '%s' % testmsg1) #getPublicKey(request))
        encrypt_file(FILE0, FILENAME, '%s' % testmsg1)
        with open(FILENAME ,'rw') as f:
            mile = File(f)
            current_user = request.user
            newdoc = Document(docfile=mile, uploader=current_user.id)
            newdoc.save()
        #documents = Document.objects.all()
        os.remove(FILENAME)
        os.remove(FILE0)
            # os.remove(FILENAME)

        d=Document.objects.get(docfile='documents/'+FILENAME0)
        #d=get_object_or_404(Document, docfile='documents/'+FILENAME0)
        d.delete()
        return HttpResponseRedirect(reverse('liss'))

    elif request.method == 'POST' and (request.POST.get('decrypt')=="Decrypt"):
        # FILENAME0 =request.POST.get('filename')[:-12]
        FILENAME0 =request.POST.get('filename')
        FILENAME0 =FILENAME0[17:]
        DECRYPTEDFILENAME = FILENAME0[:-4]
        user = request.user.username
        user = user.encode('utf-8')
        FILENAME = os.path.join(BASE_DIR, 'media/documents/%s' % FILENAME0)
        DECRYPTEDFILENAME = os.path.join(BASE_DIR, 'media/documentstemp/%s' % DECRYPTEDFILENAME)
        try:
            decrypt_file(FILENAME, DECRYPTEDFILENAME, b'%s' % user)
        except (AssertionError,IntegrityError):
            raise Http404("invalid private key")
        with open(DECRYPTEDFILENAME,'rw') as f:
            mile = File(f)
            current_user = request.user
            newdoc = Document(docfile=mile, uploader=current_user.id)
            newdoc.save()
            # documents = Document.objects.all()
            os.remove(FILENAME)
            os.remove(DECRYPTEDFILENAME)
            d=Document.objects.get(docfile='documents/'+FILENAME0)
            #d=get_object_or_404(Document,docfile='documents/'+FILENAME0)
            d.delete()
        return HttpResponseRedirect(reverse('liss'))
    elif request.method == 'POST' and (request.POST.get('delete')=="Delete"):
        FILENAME0 =request.POST.get('filename')
        FILENAME0 =FILENAME0[17:]
        FILENAME = os.path.join(BASE_DIR, 'media/documents/%s' % FILENAME0)
        d=Document.objects.get(docfile='documents/'+FILENAME0)
        d.delete()
        os.remove(FILENAME)
        return HttpResponseRedirect(reverse('liss'))
    else:
        return render(request, 'myapp/list.html')


"""
def handler404(request):
    return render_to_response('404.html')

def handler500(request):
    return render_to_response('500.html')

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
"""
# def dencc(request):
#     pass