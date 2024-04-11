---
layout: splash
permalink: /Publications/
---

<style>
	.paper_icon {
		width: min(90px, 15vw);
		border-radius: 8px;
		aspect-ratio: 1/1;
		object-fit: cover;
	}
	.info {
		display: flex;
		flex-direction: column;
	}
	.author_info {
		color: black;
		text-decoration: none;
	}
	.author_info:visited {
		color: black;
	}
	.hoverable:hover {
		text-decoration: underline;
		color: black;
	}

	table {
		border-collapse: collapse;
	}

	tr {
		border-bottom: 1pt solid #8f8f8f;
	}
	td {
		border-bottom: none;
	}
</style>

<table>
<tbody>
{% assign rev_papers = site.papers | reverse %}
{% for paper in rev_papers %}
<tr>
	<td>
	{% assign full_img_path = paper.slug | prepend: "/assets/images/papers/icons/" | append: ".webp" %}
	{% assign img_exists = site.static_files | where: "path", full_img_path %}
	{% if img_exists.size > 0 %}
	<img class="paper_icon" src="{{ full_img_path }}" loading="lazy" width="90" height="90" alt="{{ paper.slug }} thumbnail" />
	{% else %}
	<div class="paper_icon" width="90" height="90"> </div>
	{% endif %}
	</td>
	<td class="info">
		<strong> {{ paper.title }} </strong>
		<span> 
		{% for author in paper.authors %}
		    {% assign author_no_suffix = author | remove: "*" %}
		    {% assign author_info = site.data.collaborators | where: "name", author_no_suffix | first %}
			{%- if author_info == nil -%}
			<span class="author_info">{{ author }}</span>
			{%- else -%}
			<a class="author_info hoverable" href="{{ author_info.url }}" target="_blank">{{ author }}</a>
			{%- endif -%}{%- if forloop.last -%}{%- else -%},{%- endif -%}
		{% endfor %}
		</span>
		<span>{{ paper.venue }} &mdash; {{ paper.date | date: "%Y" }}</span>
		<span> 
		{%- for link in paper.links -%}
			[<a href="{{ link[1] }}" target="_blank">{{ link[0] }}</a>] 
		{% endfor %}
		[<a href="{{ paper.url }}.html" target="_blank">read more</a>]
		</span>
	</td>
</tr>
{% endfor %}
</tbody>
</table>
