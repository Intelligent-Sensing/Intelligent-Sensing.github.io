---
layout: splash
author_profile: false
title: " "
header:
#   overlay_color: "#000"
#   overlay_filter: "0.0"
  image: /assets/images/computational_imaging_splash_placeholder.svg
  
---
<!-- # About
We combine computation and sensing to extract information hidden in the world around us.  -->

## Recent News
<!-- see also news.markdown -->
<style>
#RecentNews li>p {display: inline;}
</style>
<ul id="RecentNews">
{% assign news = site.data.news | sort: 'date' | reverse %}
{% for n in news limit:8 %}
  <li>
   <span><b>{{ n.date | date: "%B %-d, %Y" }}</b></span>: {{ n.description | markdownify }}
  </li>
{% endfor %}
  <li>
   <a href="news.html">View all news</a>
  </li>
</ul>

