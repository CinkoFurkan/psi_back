from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact, Link, Sublink, About, Event, Announcement, Team, Member, Blog, Subscribe, Message, Sponsor, MemberYear
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
import base64

#ibo was here

@api_view(["GET"])
def titles(request):
    links = Link.objects.filter(is_active=True)

    content = [{
            "link": link.name,
            "sublink": [sublink.name for sublink in Sublink.objects.filter(is_active=True, link=link)]
        } for link in links]

    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def about(request):
    about = About.objects.all()
    content = {
        "about": [{
            "text": i.text,
            "title": i.title,
            "image": i.image.url if i.image else None
        } for i in about]
    }

    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def event(request):
    event = Event.objects.all()
    content = {
        "event": [{
            "title": i.title,
            "location" : i.location,
            "registration_link": i.registration_link,
            "summary_link": i.summary_link if i.summary_link else None,
            "event_date" : i.event_date,
            "is_active" : i.is_active,
            "image": i.image.url if i.image else None
        } for i in event]
    }

    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def announcement(request):
    announcement = Announcement.objects.all()
    content = {
        "announcement": [{
            "title": i.title,
            "text": i.text,
            "image": i.image.url if i.image else None,
            "link": i.link if i.link else None,
            "phone_image": i.phone_image.url if i.phone_image else None,
        } for i in announcement]
    }

    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def team(request):
    team_infos = Team.objects.all().order_by('position')
    content = {
        "team_infos": [{
            "title": i.title,
            "description": i.description,
            "position": i.position,
            "image": i.image.url if i.image else None
        } for i in team_infos]
    }

    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def member(request):
    years = MemberYear.objects.all().order_by('year')
    content = {
        "years": [{
            "year": year.year,
            "members": [{
                "member_id": member.id,
                "first_name": member.first_name,
                "last_name": member.last_name,
                "team": member.team.title if member.team else None,
                "team_id": member.team.id if member.team else None,
                "title": member.team.title if member.team else None,
                "title_member": member.title,
                "university": member.university,
                "bio": member.bio,
                "linked_in": member.linkedin if member.linkedin else None,
                "email": member.email if member.email else None,
                "image": member.image.url if member.image else None,
                "position": member.position,
            } for member in year.members.all().order_by('position')]
        } for year in years]
    }
    return Response(content, status=status.HTTP_200_OK)


@api_view(["GET"])
def member_info(request, id=None, year=None):
    if id:
        try:
            member = Member.objects.get(id=id)
            content = {
                "member": {
                    "member_id": member.id,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "team": member.team.title if member.team else None,
                    "team_id": member.team.id if member.team else None,
                    "title": member.team.title if member.team else None,
                    "title_member": member.title,
                    "university": member.university,
                    "bio": member.bio,
                    "linked_in": member.linkedin if member.linkedin else None,
                    "email": member.email if member.email else None,
                    "image": member.image.url if member.image else None,
                    'position': member.position,
                    "years": [year.year for year in member.member_years.all()],
                }
            }
            return Response(content, status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
    elif year:
        try:
            member_year = MemberYear.objects.get(year=year)
            content = {
                "year": year,
                "members": [{
                    "member_id": member.id,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "team": member.team.title if member.team else None,
                    "team_id": member.team.id if member.team else None,
                    "title": member.team.title if member.team else None,
                    "title_member": member.title,
                    "university": member.university,
                    "bio": member.bio,
                    "linked_in": member.linkedin if member.linkedin else None,
                    "email": member.email if member.email else None,
                    "image": member.image.url if member.image else None,
                    "position": member.position,
                } for member in member_year.members.all()]
            }
            return Response(content, status=status.HTTP_200_OK)
        except MemberYear.DoesNotExist:
            return Response({"error": "Year not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        members = Member.objects.all().order_by('position')
        content = {
            "members": [{
                "member_id": i.id,
                "first_name": i.first_name,
                "last_name": i.last_name,
                "team": i.team.title if i.team else None,
                "team_id": i.team.id if i.team else None,
                "title": i.team.title if i.team else None,
                "title_member": i.title,
                "university": i.university,
                "bio": i.bio,
                "linked_in": i.linkedin if i.linkedin else None,
                "email": i.email if i.email else None,
                "image": i.image.url if i.image else None,
                "position": i.position,
            } for i in members]
        }
        return Response(content, status=status.HTTP_200_OK)


@api_view(["GET"])
def blog(request):

    blogs = Blog.objects.all()
    content = {
            "blogs" :  [{
                "blog_id": i.id,
                "title": i.title,
                "short_text": i.short_text,
                "text": i.text,
                "writer_f": i.writer.first_name,
                "writer_l": i.writer.last_name,
                "writer_title": i.writer.title,
                "writer_image": i.writer.image.url,
                "created_at": i.created_at,
                "updated_at": i.updated_at,
                "is_published": i.is_published,
                "views_count": i.views_count,
                "likes_count": i.likes_count,
                "image": i.image.url if i.image else None
            } for i in blogs]
        }
    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def blog_detail(request, id=None):
    if id:
        blog = Blog.objects.get(id=id)
        content = {
            "blogs" :  {
                "blog_id": blog.id,
                "title": blog.title,
                "short_text": blog.short_text,
                "text": blog.text,
                "writer_f": blog.writer.first_name,
                "writer_l": blog.writer.last_name,
                "writer_title": blog.writer.title,
                "writer_image": blog.writer.image.url,
                "created_at": blog.created_at,
                "updated_at": blog.updated_at,
                "is_published": blog.is_published,
                "views_count": blog.views_count,  
                "likes_count": blog.likes_count,
                "image": blog.image.url if blog.image else None
            }
        }
    else:
        blogs = Blog.objects.all()
        content = {
            "blogs" :  [{
                "title": i.title,
                "short_text": i.short_text,
                "text": i.text,
                "writer_f": i.writer.first_name,
                "writer_l": i.writer.last_name,
                "writer_title": i.writer.title,
                "writer_image": i.writer.image.url,
                "created_at": i.created_at,
                "updated_at": i.updated_at,
                "is_published": i.is_published,
                "views_count": i.views_count, 
                "likes_count": i.likes_count,
                "image": i.image.url if i.image else None
            } for i in blogs]
        }
    return Response(content, status=status.HTTP_200_OK)

@api_view(['POST'])
def email(request):
    user_mail = request.data.get('user_mail')
    if not user_mail:
        return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

    subscribe = Subscribe(mail=user_mail)
    subscribe.save()

    return Response({"success": "Email has been successfully subscribed."}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def contact(request):
    user_name = request.data.get("user_name")
    user_email = request.data.get("user_email")
    subject = request.data.get("subject")
    message = request.data.get("message")

    contact = Contact(
        user_name=user_name,
        user_email=user_email,
        subject=subject,
        message=message,
    )
    contact.save()
    return Response({"success": "Email has been successfully subscribed."}, status=status.HTTP_201_CREATED)


def mail_sender(request=None, message_id=None):
    emails = Subscribe.objects.all()
    user_emails = [mail_.mail for mail_ in emails]

    try:
        if message_id:
            message_obj = Message.objects.get(id=message_id)
        else:
            message_obj = Message.objects.latest('id')
    except Message.DoesNotExist:
        print("Message not found.")
        return  

    subject = message_obj.subject
    message_text = message_obj.message
    title = message_obj.title
    sub_title = message_obj.sub_title

    image_data = ""
    if message_obj.image:
        image_path = message_obj.image.path
        with open(image_path, "rb") as img_file:
            image_data = base64.b64encode(img_file.read()).decode('utf-8')
    
    html_message = render_to_string('index.html', {
        'subject': subject,
        'title': title,
        'sub_title': sub_title,
        'message': message_text,
        'image_data': image_data,
    })

    from_email = "PsiNous Öğrenci Topluluğu <{}>".format(settings.EMAIL_HOST_USER)

    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=[settings.EMAIL_HOST_USER], 
        bcc=user_emails  
    )
    
    email.content_subtype = "html"

    email.send()

@api_view(['PUT'])
def like_view(request):
    new_like =  request.data.get('new_like')
    new_view =  request.data.get('new_view')
    blog_id =  request.data.get('id')
    try:
        blog = Blog.objects.get(id=blog_id)
    except:
        return Response({"message": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)

    blog.likes_count = new_like
    blog.views_count = new_view

    blog.save()
    return Response({"message": "Blog updated successfully."}, status=200)

 
@api_view(['GET'])
def sponsor(request):
    sponsors = Sponsor.objects.all().order_by('position')
    content = {
        "sponsors": [
            {
                'id': sponsor.id,
                "text": sponsor.text,
                'image': sponsor.image.url if sponsor.image and hasattr(sponsor.image, 'url') else None,
                'position': sponsor.position
            } for sponsor in sponsors
        ]
    }
    return Response(content)

