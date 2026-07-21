---
layout: splash
author_profile: false
title: " "
header:
#   overlay_color: "#000"
#   overlay_filter: "0.0"
  image: /assets/images/computational_imaging_splash_placeholder.svg
  
---

<style>
  .lab-tagline {
    max-width: 860px;
    margin: 0 auto 2.5em auto;
    text-align: center;
    align-self: center;
    font-size: 1.25em;
    line-height: 1.55;
    color: #333;
  }
  /* Center the whole home content column regardless of theme layout */
  .page__content > .lab-tagline,
  .page__content > .recruit-banner,
  .page__content > .section-heading,
  .page__content > .section-sub { margin-left: auto; margin-right: auto; }
  .section-heading {
    text-align: center;
    margin: 1.5em 0 0.25em 0;
  }
  .section-sub {
    text-align: center;
    color: #777;
    margin: 0 auto 1.5em auto;
    max-width: 640px;
  }

  /* Research areas */
  .areas-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.1em;
    max-width: 960px;
    margin: 0 auto 3em auto;
  }
  .area-card {
    border: 1px solid #e3e3e3;
    border-radius: 10px;
    padding: 1.25em;
    background: #fff;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  }
  .area-card h3 { margin: 0 0 0.4em 0; font-size: 1.05em; }
  .area-card p { margin: 0; font-size: 0.9em; color: #555; line-height: 1.5; }

  /* Featured work */
  .featured-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.25em;
    max-width: 960px;
    margin: 0 auto 3em auto;
  }
  .featured-card {
    border: 1px solid #e3e3e3;
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  .featured-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.10);
  }
  .featured-card a { text-decoration: none; color: inherit; }
  .featured-card img {
    width: 100%;
    aspect-ratio: 16/9;
    object-fit: cover;
    display: block;
  }
  .featured-card .caption { padding: 0.85em 1em; }
  .featured-card .caption .venue {
    font-size: 0.72em;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #c8102e;
    font-weight: 600;
  }
  .featured-card .caption .title {
    display: block;
    font-size: 0.92em;
    line-height: 1.35;
    margin-top: 0.2em;
    color: #222;
  }

  /* Recruiting banner */
  .recruit-banner {
    max-width: 960px;
    margin: 0 auto 3em auto;
    padding: 1.5em 2em;
    border-radius: 10px;
    background: #f7f2f2;
    border: 1px solid #ecd9dc;
    text-align: center;
  }
  .recruit-banner a.btn {
    display: inline-block;
    margin-top: 0.75em;
    background: #c8102e;
    color: #fff !important;
    padding: 0.55em 1.4em;
    border-radius: 999px;
    font-weight: 600;
    text-decoration: none;
  }

  #RecentNews li>p {display: inline;}
  #RecentNews { max-width: 860px; margin: 0 auto; }

  .press-list { max-width: 860px; margin: 0 auto; list-style: none; padding: 0; }
  .press-list li { padding: .75rem 0; border-bottom: 1px solid #f0f0f0; }
  .press-list li:last-child { border-bottom: 0; }
  .press-outlet { display: block; font-size: .8rem; font-weight: 600; color: #757575; letter-spacing: .02em; margin-bottom: .15rem; }
  .press-also { color: #757575; font-size: .9em; }
</style>

<p class="lab-tagline">
The Intelligent Sensing Lab combines machine learning, statistical signal processing, and
physics to see far beyond the limits of conventional cameras and sensors.
</p>

<div class="recruit-banner" markdown="1">
### We're recruiting!
We have openings for **postdocs &amp; research scientists**.
<a class="btn" href="/Openings/">See Open Positions</a>
</div>

<h2 class="section-heading">Recent Updates</h2>
<!-- see also news.markdown -->
<ul id="RecentNews">
{% assign news = site.data.news | sort: 'date' | reverse %}
{% for n in news limit:8 %}
  <li>
   <span><b>{{ n.date | date: "%B %-d, %Y" }}</b></span>: {{ n.description | markdownify }}
  </li>
{% endfor %}
  <li>
   <a href="news.html">View all updates</a>
  </li>
</ul>

<h2 class="section-heading">Press</h2>
<ul class="press-list">
  <li>
    <span class="press-outlet">PetaPixel · June 2023</span>
    <a href="https://petapixel.com/2023/06/29/scientists-can-now-reconstruct-rooms-from-eye-reflections-in-photos/" target="_blank" rel="noopener">Scientists Can Now Reconstruct Rooms From Eye Reflections in Photos</a>
  </li>
  <li>
    <span class="press-outlet">Science · June 2023</span>
    <a href="https://www.science.org/doi/full/10.1126/sciadv.adg4671" target="_blank" rel="noopener">Neural wavefront shaping featured on the Science homepage</a>
  </li>
  <li>
    <span class="press-outlet">Gizmodo · September 2021</span>
    <a href="https://gizmodo.com/a-single-laser-fired-through-a-keyhole-can-expose-every-1847638281" target="_blank" rel="noopener">A Single Laser Fired Through a Keyhole Can Expose Everything Inside a Room</a>
  </li>
  <li>
    <span class="press-outlet">IEEE Spectrum · January 2020</span>
    <a href="https://spectrum.ieee.org/seeing-around-corner-lasers-speckle" target="_blank" rel="noopener">Seeing Around Corners with Lasers—and Speckle</a>
    <span class="press-also">(also covered by <a href="https://www.thetimes.co.uk/article/soldiers-could-see-round-corners-after-ai-breakthrough-qqwfcf39t" target="_blank" rel="noopener">The Times</a> and <a href="https://www.telegraph.co.uk/technology/2020/01/16/ai-allows-self-driving-cars-see-around-corners/" target="_blank" rel="noopener">The Telegraph</a>)</span>
  </li>
</ul>
