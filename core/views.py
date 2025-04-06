from itertools import chain
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User , auth
from django.contrib import messages

from core.models import FollowerCount, Post, Profile, LikePost

@login_required(login_url='signin')
def index(request):
    user_profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            'id_user': request.user.id
        }
    )
    posts = Post.objects.all().order_by('-created_at')

    user_following_list = []
    feed = []

    user_following = FollowerCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames).order_by('-created_at')
        feed.append(feed_lists)

    feed_lists = list(chain(*feed))
    return render(request, 'index.html', {'user_profile': user_profile, 'posts': feed_lists})

@login_required(login_url='signin')
def search(request):
    user_objects = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_objects)

    if request.method == 'POST':
        username = request.POST.get('username')
        username_object = User.objects.filter(username__icontains=username).exclude(username=request.user.username)
        username_profile = []
        username_profile_list = []
        for users in username_object:
            username_profile_list.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)

        username_profile_list = list(chain(*username_profile_list))

    return render(request, 'search.html', {'user_profile': user_profile, 'username': username})

@login_required(login_url='signin')
def posts(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        user = request.user.username

        if caption and image:
            post = Post.objects.create(user=user, caption=caption, image=image)
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('/')
        else:
            messages.error(request, 'Please fill in all fields.')
    else:
        return redirect('/')

@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes += 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes -= 1
        post.save()
        return redirect('/')
    
@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_posts_length = user_posts.count()

    follower = request.user.username
    user = pk
    if FollowerCount.objects.filter(follower=follower, user=user).exists():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = FollowerCount.objects.filter(user=pk).count()
    user_following = FollowerCount.objects.filter(follower=pk).count()

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_posts_length': user_posts_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
        }
    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST.get('follower')
        user = request.POST.get('user')

        if FollowerCount.objects.filter(follower=follower, user=user).exists():
            delete_follower = FollowerCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/' + user + '/')
        else:
            new_follower = FollowerCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/' + user + '/')
    else:

        return redirect('/')

@login_required(login_url='signin')
def setting(request):
        user_profile = Profile.objects.get(user=request.user)

        if request.method == 'POST':
            bio = request.POST.get('bio')
            location = request.POST.get('location')
            profile_picture = request.FILES.get('profile_picture')

            user_profile.bio = bio
            user_profile.location = location

            if profile_picture:
                user_profile.profile_picture = profile_picture

            user_profile.save() 
            messages.success(request, 'Profile updated successfully.')
            return redirect('setting')

        return render(request, 'setting.html', {'user_profile': user_profile})

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')



        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken.')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already in use.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Account created successfully.')

                user_login = auth.authenticate(username=username, password=password)
                if user_login is not None:
                    auth.login(request, user_login)
                    messages.success(request, 'Logged in successfully.')

                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
    

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials.')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
@login_required(login_url='signin')   
def logout(request):
    auth.logout(request)
    return redirect('signin')   