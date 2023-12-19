import html
import subprocess


def img_html(img_path, img_alt, style=1):
    if style == 0:
        return f'<img src="{img_path}" alt="{img_alt}">\n'
    elif style == 1:
        return f'''
      <div class="col">
            <div class="img-thumb">
              <img class="img-fluid" src="{img_path}" alt="{img_alt}">
              <div class="bottom-left"><a class="lightbox" href="{img_path}" style="color: white;">
                <i class="fa fa-plus"></i>
              </a></div>
          </div>
      </div>'''
  # <i class="lni-plus"></i>

gallery_dir = "assets/img/event gallery/"
# read the file names
# ls_results = subprocess.check_output(f"ls {gallery_dir} -p").decode("utf-8").split("\n")
ls_results = subprocess.run(f"ls -p '{gallery_dir}'", shell=True, capture_output=True)
ls_output = ls_results.stdout.decode("utf-8")
ls_out_list = ls_output.split("\n")
# those that end with / are directories
file_names = [file_name for file_name in ls_out_list if not file_name.endswith("/")]
sub_dir_names = [file_name for file_name in ls_out_list if file_name.endswith("/")]
# remove the trailing /
sub_dir_names = [sub_dir_name[:-1] for sub_dir_name in sub_dir_names]
# keep the file names that end with .jpg, .jpeg or .png, or their capitalised versions
file_names = [file_name for file_name in file_names if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png") or file_name.endswith(".JPG") or file_name.endswith(".JPEG") or file_name.endswith(".PNG")]

print("Files: ",file_names)

html_text = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <title>Gallery - ISM 2023</title>


    <link rel="shortcut icon" href="./assets/iitblogo.ico" type="image/x-icon">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css" >
    <!-- Icon -->
    <link rel="stylesheet" type="text/css" href="assets/fonts/line-icons.css">
    <!-- Slicknav -->
    <link rel="stylesheet" type="text/css" href="assets/css/slicknav.css">
    <!-- Nivo Lightbox -->
    <link rel="stylesheet" type="text/css" href="assets/css/nivo-lightbox.css" >
    <!-- Animate -->
    <link rel="stylesheet" type="text/css" href="assets/css/animate.css">
    <!-- Main Style -->
    <link rel="stylesheet" type="text/css" href="assets/css/main.css">
    <!-- Responsive Style -->
    <link rel="stylesheet" type="text/css" href="assets/css/responsive.css">

<style>
    .photo-gallery {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        grid-gap: 10px;
      }
      
      .photo-gallery img {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 8px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease-in-out;
      }
      
      .photo-gallery img:hover {
        transform: scale(1.05);
      }

      .bottom-left {
  position: absolute;
  bottom: 0px;
  left: 20px;
}
    </style>

  </head>
  <body>

    <!-- Header Area wrapper Starts -->
    <header id="header-wrap">
      <!-- Navbar Start -->
      <nav class="navbar navbar-expand-lg fixed-top scrolling-navbar">
        <div class="container">
          <!-- Brand and toggle get grouped for better mobile display -->
          <div class="navbar-header">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main-navbar" aria-controls="main-navbar" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
              <span class="icon-menu"></span>
              <span class="icon-menu"></span>
              <span class="icon-menu"></span>
            </button>
            <a href="index.html" class="navbar-brand"><img src="assets/img/iitblogo.png" style="width: 60px; margin: 10px -10px;" alt=""></a><a href="index.html" class="navbar-brand"><img src="assets/img/ictp.png" style="width: 60px; margin: 10px 0px;" alt=""></a> <span style="color:black; font-weight: 1000; font-size: 17px;">Indian Strings Meeting 2023</span>
          </div>
          <!-- <div class="collapse navbar-collapse" id="main-navbar">
            <ul class="navbar-nav mr-auto w-100 justify-content-end">
              <li class="nav-item active">
                <a class="nav-link" href="#header-wrap">
                  Home
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#about">
                  Talks
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#schedules">
                  Organising Committee
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#team">
                  Participants
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="gallery.html">
                  Schedule
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#faq">
                  Registration
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#sponsors">
                  How to Reach?
                </a>
              </li>
            </ul>
          </div>
        </div> -->

        <!-- Mobile Menu Start -->
        <ul class="mobile-menu">
          <li>
            <a class="page-scrool" href="#header-wrap">Home</a>
          </li>
          <li>
            <a class="page-scrool" href="#about">About</a>
          </li>
          <li>
             <a class="page-scroll" href="#schedules">Schedules</a>
          </li>
          <li>
            <a class="page-scroll" href="#team">Speakers</a>
          </li>
          <li>
            <a class="page-scroll" href="gallery.html">Gallery</a>
          </li>
          <li>
            <a class="page-scroll" href="#faq">Faq</a>
          </li>
          <li>
            <a class="page-scroll" href="#sponsors">Sponsors</a>
          </li>
          <li>
            <a class="page-scroll" href="#pricing">pricing</a>
          </li>
          <li>
            <a class="page-scroll" href="#google-map-area">Contact</a>
          </li>
        </ul>
        <!-- Mobile Menu End -->

      </nav>
      <!-- Navbar End -->

      <!-- Main Carousel Section Start -->
      <div id="main-slide" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#main-slide" data-slide-to="0" class="active"></li>
          <!-- <li data-target="#main-slide" data-slide-to="1"></li> -->
          <!-- <li data-target="#main-slide" data-slide-to="2"></li> -->
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="d-block w-100" src="assets/img/background/bg-main.jpeg" alt="First slide">
            <div class="carousel-caption d-md-block" style="background: rgba(0,0,0,0.5);
            height: fit-content;
            border-radius: 22px;">
              <p class="fadeInUp wow" data-wow-delay=".6s">Indian Strings Meeting 2023
                </p>
              <h1 class="wow fadeInDown heading" data-wow-delay=".4s">
                Event Gallery
                </h1>
                
              <!-- <a href="#" class="fadeInLeft wow btn btn-common btn-lg" data-wow-delay=".6s">Register</a>
              <a href="#" class="fadeInRight wow btn btn-border btn-lg" data-wow-delay=".6s">Explore More</a> -->
            </div>
          </div>
          <!-- <div class="carousel-item">
            <img class="d-block w-100" src="assets/img/slider/slide2.jpg" alt="Second slide">
            <div class="carousel-caption d-md-block">
              <p class="fadeInUp wow" data-wow-delay=".6s">Indian Strings Meeting 2023</p>
              <h1 class="wow bounceIn heading" data-wow-delay=".7s">XX Speakers from across the country</h1>
              <a href="#" class="fadeInUp wow btn btn-common btn-lg" data-wow-delay=".8s" style="color: black;">Explore</a>            </div>
          </div> -->
          <!-- <div class="carousel-item">
            <img class="d-block w-100" src="assets/img/slider/slide3.jpeg" alt="Third slide">
            <div class="carousel-caption d-md-block">
              <p class="fadeInUp wow" data-wow-delay=".6s" style="color: black;">Biennial International Conference of String theorists</p>
              <h1 class="wow fadeInUp heading" data-wow-delay=".6s" style="color: black;">Book Your Seat Now!</h1>
              <a href="#" class="fadeInUp wow btn btn-common btn-lg" data-wow-delay=".8s" style="color: black;">Explore</a>
            </div>
          </div> -->
        </div>
        <!-- <a class="carousel-control-prev" href="#main-slide" role="button" data-slide="prev">
          <span class="carousel-control" aria-hidden="true"><i class="lni-chevron-left"></i></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#main-slide" role="button" data-slide="next">
          <span class="carousel-control" aria-hidden="true"><i class="lni-chevron-right"></i></span>
          <span class="sr-only">Next</span>
        </a> -->
      </div>
      <!-- Main Carousel Section End -->
      

    </header>
 '''


# sort the sub_dir_names
# If there is a sub_dir named Talks, then it should come first
# then any sub_dir with "poster" in its name
# then the one with women in its name
sub_dir_names.sort(key=lambda x: "women" in x.lower(), reverse=True)
sub_dir_names.sort(key=lambda x: "poster" in x.lower(), reverse=True)
sub_dir_names.sort(key=lambda x: "talks" in x.lower(), reverse=True)
print("Directories (in order): ",sub_dir_names)

for sub_dir in sub_dir_names:
    # start a new section
    html_text += f'''<section id="about" class="section-padding">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="section-title-header text-center">
              <h1 class="section-title wow fadeInUp" data-wow-delay="0.2s">{sub_dir}</h1>
            </div>
          </div>
        </div>
      </div>
    '''
    # read the images inside the sub_dir
    sub_dir_path = gallery_dir + sub_dir + "/"
    # ls_results = subprocess.check_output(f"ls -p '{sub_dir_path}'").decode("utf-8").split("\n")
    subdir_ls_out_list = subprocess.run(f"ls -p '{sub_dir_path}'", shell=True, capture_output=True).stdout.decode("utf-8").split("\n")
    # those that end with / are directories
    file_names_sub_dir = [file_name for file_name in subdir_ls_out_list if not file_name.endswith("/")]
    # keep the file names that end with .jpg, .jpeg or .png
    file_names_sub_dir = [file_name for file_name in file_names_sub_dir if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png") or file_name.endswith(".JPG") or file_name.endswith(".JPEG") or file_name.endswith(".PNG")]
    print(f"Files in sub dir {sub_dir}: ",file_names_sub_dir)

    html_text += '\n<div class="photo-gallery">\n'
    for file_name in file_names_sub_dir:
        html_text += img_html(sub_dir_path + "/" + file_name, file_name, style=1)
    html_text += '</div>\n'
    html_text += '</section>\n'

# now add the images that are not in any sub_dir
if len(file_names) > 0:
  html_text += f'''<section id="about" class="section-padding">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="section-title-header text-center">
              <h1 class="section-title wow fadeInUp" data-wow-delay="0.2s">Other Images</h1>
            </div>
          </div>
        </div>
      </div>

    <div class="photo-gallery">
    '''
  for file_name in file_names:
      html_text += img_html(gallery_dir + "/" + file_name, file_name, style=1)
  html_text += '</div>\n'
  html_text += '</section>\n'

# now for the end of the file
html_text += '''
    <!-- Map Section Start -->
    <section id="google-map-area">
      <div class="container-fluid">
        <div class="row">
        </div>
      </div>
    </section>
    <!-- Map Section End -->

    <!-- Footer Section Start -->
    <footer class="footer-area section-padding">
      <div class="container">
        <div class="row">
          <div class="col-md-6 col-lg-3 col-sm-6 col-xs-12 wow fadeInUp" data-wow-delay="0.2s">
            <h3><img src="assets/img/iitblogo.png" alt="" style="width:80px; float: left;"></h3>
            <h3><img src="assets/img/ictp2.png" alt="" style="width:80px; margin-top: -10px; margin-left: 10px;"></h3>
            <p>
                Indian Institute of Technology Bombay, <br> Powai, Maharashtra - 400076 <a href="mailto:ism2023@phy.iitb.ac.in">ism2023@phy.iitb.ac.in</a>
            </p>
          </div>
          <div class="col-md-6 col-lg-3 col-sm-6 col-xs-12 wow fadeInUp" data-wow-delay="0.4s">
            <h3>QUICK LINKS</h3>
            <ul>
              <li><a href="./index.html#about">About Conference</a></li>
              <li><a href="./index.html#speakers">Our Speakers</a></li>
              <li><a href="./index.html#schedules">Event Schedule</a></li>
              <li><a href="./gallery.html">Event Photo Gallery</a></li>
            </ul>
          </div>
          <!-- <div class="col-md-6 col-lg-3 col-sm-6 col-xs-12 wow fadeInUp" data-wow-delay="0.6s">
            <h3>RECENT POSTS</h3>
            <ul class="image-list">
              <li>
                <figure class="overlay">
                  <img class="img-fluid" src="assets/img/art/a1.jpg" alt="">
                </figure>
                <div class="post-content">
                  <h6 class="post-title"> <a href="blog-single.html">Lorem ipsm dolor sumit.</a> </h6>
                  <div class="meta"><span class="date">October 12, 2018</span></div>
                </div>
              </li>
              <li>
                <figure class="overlay">
                  <img class="img-fluid" src="assets/img/art/a2.jpg" alt="">
                </figure>
                <div class="post-content">
                  <h6 class="post-title"><a href="blog-single.html">Lorem ipsm dolor sumit.</a></h6>
                  <div class="meta"><span class="date">October 12, 2018</span></div>
                </div>
              </li>
            </ul>
          </div> -->
          <!-- <div class="col-md-6 col-lg-3 col-sm-6 col-xs-12 wow fadeInUp" data-wow-delay="0.8s">
            <h3>SUBSCRIBE US</h3>
            <div class="widget">
              <div class="newsletter-wrapper">
                <form method="post" id="subscribe-form" name="subscribe-form" class="validate">
                  <div class="form-group is-empty">
                    <input type="email" value="" name="Email" class="form-control" id="EMAIL" placeholder="Your email" required="">
                    <button type="submit" name="subscribe" id="subscribes" class="btn btn-common sub-btn"><i class="lni-pointer"></i></button>
                    <div class="clearfix"></div>
                  </div>
                </form>
              </div>
            </div> -->
            <!-- /.widget -->
            <div class="widget">
              <h5 class="widget-title">FOLLOW IITB ON</h5>
              <ul class="footer-social">
                <li><a class="facebook" href="https://www.facebook.com/iitbombay/"><i class="lni-facebook-filled"></i></a></li>
                <li><a class="twitter" href="https://twitter.com/iitbombay"><i class="lni-twitter-filled"></i></a></li>
                <li><a class="linkedin" href="https://www.linkedin.com/school/indian-institute-of-technology-bombay/"><i class="lni-linkedin-filled"></i></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </footer>
    <!-- Footer Section End -->

    <div id="copyright">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <div class="site-info">
              <p>© Designed and Developed by <a href="http://homepages.iitb.ac.in/~kandarp.solanki" target="_blank" style="color: #E91E63; text-decoration: underline;">Kandarp Solanki</a><br>
              Updated and Maintained by <a href="https://inspirehep.net/authors/2546942?ui-citation-summary=true" target="_blank" style="color: #E91E63; text-decoration: underline;">Archana Maji</a>, <a href="https://kabir200310.wixsite.com/kabir-physics3208" target="_blank" style="color: #E91E63; text-decoration: underline;">Kabir Bajaj</a> & <a href="https://rehmatschawla.github.io" target="_blank" style="color: #E91E63; text-decoration: underline;">Rehmat Singh Chawla</a></p>
            </div>      
          </div>
        </div>
      </div>
    </div>

    <!-- Go to Top Link -->
    <a href="#" class="back-to-top">
    	<i class="lni-chevron-up"></i>
    </a>

    <div id="preloader">
      <div class="sk-circle">
        <div class="sk-circle1 sk-child"></div>
        <div class="sk-circle2 sk-child"></div>
        <div class="sk-circle3 sk-child"></div>
        <div class="sk-circle4 sk-child"></div>
        <div class="sk-circle5 sk-child"></div>
        <div class="sk-circle6 sk-child"></div>
        <div class="sk-circle7 sk-child"></div>
        <div class="sk-circle8 sk-child"></div>
        <div class="sk-circle9 sk-child"></div>
        <div class="sk-circle10 sk-child"></div>
        <div class="sk-circle11 sk-child"></div>
        <div class="sk-circle12 sk-child"></div>
      </div>
    </div>

    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="assets/js/jquery-min.js"></script>
    <script src="assets/js/popper.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/jquery.countdown.min.js"></script>
    <script src="assets/js/jquery.nav.js"></script>
    <script src="assets/js/jquery.easing.min.js"></script>
    <script src="assets/js/wow.js"></script>
    <script src="assets/js/jquery.slicknav.js"></script>
    <script src="assets/js/nivo-lightbox.js"></script>
    <script src="assets/js/main.js"></script>
  </body>
</html>
'''

with open("gallery.html","w") as f:
    f.write(html_text)
