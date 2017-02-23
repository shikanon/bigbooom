#coding:utf8
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigbooom.settings")
django.setup()

from moderna.models import Category, Paper
from citizen.models import Citizen
from django.contrib.auth.models import User

category_all_kwargs = [
    {'name':u'游戏玩家', 'introduction': '单机游戏、游戏攻略'},
    {'name': u'新闻资讯', 'introduction': '各类新闻、新闻快报'},# 央视新闻
    {'name': u'二次元', 'introduction': '二次元资讯、点评'},
    {'name': u'技术前沿', 'introduction': '技术博客、前沿资讯'},# 开发者头条、InfoQ
    {'name': u'娱乐八卦', 'introduction': '搞笑段子、娱乐新闻、八卦新闻'},# UC神评论
    {'name': u'女性生活', 'introduction': '美丽、时尚、女性、生活'},# 蒙咪
    {'name': u'金融投资', 'introduction': '投资热点、今日头条'},# 36kr
    {'name': u'同性社区', 'introduction': '未知的领域，等待你加入，更精彩'},
    {'name': u'算法建模', 'introduction': '智慧资讯、科技盛宴、人工智能'},# 机器之心、新智元、open-open
    {'name': u'高出不胜寒', 'introduction': '起舞弄清影，高学历自娱自乐'},# 中科院
]

for kwargs in category_all_kwargs:
    try:
        category = Category(**kwargs)
        category.save()
    except:
        pass

all_kwargs = {'title':'Django',
              'content':'''<div id="top">
<div class="container"><a class="logo" href="https://www.djangoproject.com/">Django</a>
<p class="meta">The web framework for perfectionists with deadlines.</p>
<div class="nav-menu-on">
<ul>
<li><a href="https://www.djangoproject.com/start/overview/">OVERVIEW</a></li>
<li><a href="https://www.djangoproject.com/download/">DOWNLOAD</a></li>
<li class="active"><a href="https://docs.djangoproject.com/">DOCUMENTATION</a></li>
<li><a href="https://www.djangoproject.com/weblog/">NEWS</a></li>
<li><a href="https://www.djangoproject.com/community/">COMMUNITY</a></li>
<li><a href="https://code.djangoproject.com/">CODE</a></li>
<li><a href="https://www.djangoproject.com/foundation/">ABOUT</a></li>
<li><a href="https://www.djangoproject.com/fundraising/">♥ DONATE</a></li>
</ul>
</div>
</div>
</div>
<div class="copy-banner">
<div class="container">
<h1><a href="https://docs.djangoproject.com/en/1.10/">Documentation</a></h1>
</div>
</div>
<div id="billboard"></div>
<div class="container sidebar-right">
<div>
<div id="version-switcher">
<ul class="language-switcher" id="doc-languages">
<li class="current" title="Click on the links on the left to switch to another language."><span>Language: <strong>en</strong></span></li>
</ul>
<ul class="version-switcher" id="doc-versions">
<li class="current" title="This document describes Django 1.10. Click on the links on the left to see other versions."><span>Documentation version: <strong>1.10</strong></span></li>
</ul>
</div>
<div id="docs-content">
<div class="section" id="s-writing-your-first-django-app-part-3"><span id="writing-your-first-django-app-part-3"></span>
<h1>Writing your first Django app, part 3<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#writing-your-first-django-app-part-3" title="Permalink to this headline">¶</a></h1>
<p>This tutorial begins where <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial02/"><span class="doc">Tutorial 2</span></a> left off. We’re continuing the Web-poll application and will focus on creating the public interface – “views.”</p>
<div class="section" id="s-overview"><span id="overview"></span>
<h2>Overview<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#overview" title="Permalink to this headline">¶</a></h2>
<p>A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. For example, in a blog application, you might have the following views:</p>
<ul class="simple">
<li>Blog homepage – displays the latest few entries.</li>
<li>Entry “detail” page – permalink page for a single entry.</li>
<li>Year-based archive page – displays all months with entries in the given year.</li>
<li>Month-based archive page – displays all days with entries in the given month.</li>
<li>Day-based archive page – displays all entries in the given day.</li>
<li>Comment action – handles posting comments to a given entry.</li>
</ul>
<p>In our poll application, we’ll have the following four views:</p>
<ul class="simple">
<li>Question “index” page – displays the latest few questions.</li>
<li>Question “detail” page – displays a question text, with no results but with a form to vote.</li>
<li>Question “results” page – displays results for a particular question.</li>
<li>Vote action – handles voting for a particular choice in a particular question.</li>
</ul>
<p>In Django, web pages and other content are delivered by views. Each view is represented by a simple Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).</p>
<p>Now in your time on the web you may have come across such beauties as “ME2/Sites/dirmod.asp?sid=&amp;type=gen&amp;mod=Core+Pages&amp;gid=A6CD4967199A42D9B65B1B”. You will be pleased to know that Django allows us much more elegant <em>URL patterns</em> than that.</p>
<p>A URL pattern is simply the general form of a URL - for example: <code class="docutils literal"><span class="pre">/newsarchive/&lt;year&gt;/&lt;month&gt;/</span></code>.</p>
<p>To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns (described as regular expressions) to views.</p>
<p>This tutorial provides basic instruction in the use of URLconfs, and you can refer to <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/urlresolvers/#module-django.urls" title="django.urls"><code class="xref py py-mod docutils literal"><span class="pre">django.urls</span></code></a> for more information.</p>
</div>
<div class="section" id="s-writing-more-views"><span id="writing-more-views"></span>
<h2>Writing more views<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#writing-more-views" title="Permalink to this headline">¶</a></h2>
<p>Now let’s add a few more views to <code class="docutils literal"><span class="pre">polls/views.py</span></code>. These views are slightly different, because they take an argument:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/views.py</div>
<div class="highlight">
<pre><span></span><span class="k">def</span> <span class="nf">detail</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="s2">"You're looking at question </span><span class="si">%s</span><span class="s2">."</span> <span class="o">%</span> <span class="n">question_id</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">results</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="s2">"You're looking at the results of question </span><span class="si">%s</span><span class="s2">."</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="n">response</span> <span class="o">%</span> <span class="n">question_id</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">vote</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="s2">"You're voting on question </span><span class="si">%s</span><span class="s2">."</span> <span class="o">%</span> <span class="n">question_id</span><span class="p">)</span>
</pre>
</div>
</div>
<p>Wire these new views into the <code class="docutils literal"><span class="pre">polls.urls</span></code> module by adding the following <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/urls/#django.conf.urls.url" title="django.conf.urls.url"><code class="xref py py-func docutils literal"><span class="pre">url()</span></code></a> calls:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/urls.py</div>
<div class="highlight">
<pre><span></span><span class="kn">from</span> <span class="nn">django.conf.urls</span> <span class="k">import</span> <span class="n">url</span>

<span class="kn">from</span> <span class="nn">.</span> <span class="k">import</span> <span class="n">views</span>

<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
    <span class="c1"># ex: /polls/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'index'</span><span class="p">),</span>
    <span class="c1"># ex: /polls/5/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^(?P&lt;question_id&gt;[0-9]+)/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'detail'</span><span class="p">),</span>
    <span class="c1"># ex: /polls/5/results/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^(?P&lt;question_id&gt;[0-9]+)/results/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">results</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'results'</span><span class="p">),</span>
    <span class="c1"># ex: /polls/5/vote/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^(?P&lt;question_id&gt;[0-9]+)/vote/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">vote</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'vote'</span><span class="p">),</span>
<span class="p">]</span>
</pre>
</div>
</div>
<p>Take a look in your browser, at “/polls/34/”. It’ll run the <code class="docutils literal"><span class="pre">detail()</span></code> method and display whatever ID you provide in the URL. Try “/polls/34/results/” and “/polls/34/vote/” too – these will display the placeholder results and voting pages.</p>
<p>When somebody requests a page from your website – say, “/polls/34/”, Django will load the <code class="docutils literal"><span class="pre">mysite.urls</span></code> Python module because it’s pointed to by the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-ROOT_URLCONF"><code class="xref std std-setting docutils literal"><span class="pre">ROOT_URLCONF</span></code></a> setting. It finds the variable named <code class="docutils literal"><span class="pre">urlpatterns</span></code> and traverses the regular expressions in order. After finding the match at <code class="docutils literal"><span class="pre">'^polls/'</span></code>, it strips off the matching text (<code class="docutils literal"><span class="pre">"polls/"</span></code>) and sends the remaining text – <code class="docutils literal"><span class="pre">"34/"</span></code> – to the ‘polls.urls’ URLconf for further processing. There it matches <code class="docutils literal"><span class="pre">r'^(?P&lt;question_id&gt;[0-9]+)/$'</span></code>, resulting in a call to the <code class="docutils literal"><span class="pre">detail()</span></code> view like so:</p>
<div class="highlight-default">
<div class="highlight">
<pre><span></span><span class="n">detail</span><span class="p">(</span><span class="n">request</span><span class="o">=&lt;</span><span class="n">HttpRequest</span> <span class="nb">object</span><span class="o">&gt;</span><span class="p">,</span> <span class="n">question_id</span><span class="o">=</span><span class="s1">'34'</span><span class="p">)</span>
</pre>
</div>
</div>
<p>The <code class="docutils literal"><span class="pre">question_id='34'</span></code> part comes from <code class="docutils literal"><span class="pre">(?P&lt;question_id&gt;[0-9]+)</span></code>. Using parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the view function; <code class="docutils literal"><span class="pre">?P&lt;question_id&gt;</span></code> defines the name that will be used to identify the matched pattern; and <code class="docutils literal"><span class="pre">[0-9]+</span></code> is a regular expression to match a sequence of digits (i.e., a number).</p>
<p>Because the URL patterns are regular expressions, there really is no limit on what you can do with them. And there’s no need to add URL cruft such as <code class="docutils literal"><span class="pre">.html</span></code> – unless you want to, in which case you can do something like this:</p>
<div class="highlight-default">
<div class="highlight">
<pre><span></span><span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^polls/latest\.html$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">index</span><span class="p">),</span>
</pre>
</div>
</div>
<p>But, don’t do that. It’s silly.</p>
</div>
<div class="section" id="s-write-views-that-actually-do-something"><span id="write-views-that-actually-do-something"></span>
<h2>Write views that actually do something<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#write-views-that-actually-do-something" title="Permalink to this headline">¶</a></h2>
<p>Each view is responsible for doing one of two things: returning an <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a> object containing the content for the requested page, or raising an exception such as <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a>. The rest is up to you.</p>
<p>Your view can read records from a database, or not. It can use a template system such as Django’s – or a third-party Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.</p>
<p>All Django wants is that <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a>. Or an exception.</p>
<p>Because it’s convenient, let’s use Django’s own database API, which we covered in <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial02/"><span class="doc">Tutorial 2</span></a>. Here’s one stab at a new <code class="docutils literal"><span class="pre">index()</span></code> view, which displays the latest 5 poll questions in the system, separated by commas, according to publication date:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/views.py</div>
<div class="highlight">
<pre><span></span><span class="kn">from</span> <span class="nn">django.http</span> <span class="k">import</span> <span class="n">HttpResponse</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>


<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="n">latest_question_list</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">'-pub_date'</span><span class="p">)[:</span><span class="mi">5</span><span class="p">]</span>
    <span class="n">output</span> <span class="o">=</span> <span class="s1">', '</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">q</span><span class="o">.</span><span class="n">question_text</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">latest_question_list</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>

<span class="c1"># Leave the rest of the views (detail, results, vote) unchanged</span>
</pre>
</div>
</div>
<p>There’s a problem here, though: the page’s design is hard-coded in the view. If you want to change the way the page looks, you’ll have to edit this Python code. So let’s use Django’s template system to separate the design from Python by creating a template that the view can use.</p>
<p>First, create a directory called <code class="docutils literal"><span class="pre">templates</span></code> in your <code class="docutils literal"><span class="pre">polls</span></code> directory. Django will look for templates in there.</p>
<p>Your project’s <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-TEMPLATES"><code class="xref std std-setting docutils literal"><span class="pre">TEMPLATES</span></code></a> setting describes how Django will load and render templates. The default settings file configures a <code class="docutils literal"><span class="pre">DjangoTemplates</span></code> backend whose <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-TEMPLATES-APP_DIRS"><code class="xref std std-setting docutils literal"><span class="pre">APP_DIRS</span></code></a> option is set to <code class="docutils literal"><span class="pre">True</span></code>. By convention <code class="docutils literal"><span class="pre">DjangoTemplates</span></code>looks for a “templates” subdirectory in each of the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-INSTALLED_APPS"><code class="xref std std-setting docutils literal"><span class="pre">INSTALLED_APPS</span></code></a>.</p>
<p>Within the <code class="docutils literal"><span class="pre">templates</span></code> directory you have just created, create another directory called <code class="docutils literal"><span class="pre">polls</span></code>, and within that create a file called <code class="docutils literal"><span class="pre">index.html</span></code>. In other words, your template should be at <code class="docutils literal"><span class="pre">polls/templates/polls/index.html</span></code>. Because of how the <code class="docutils literal"><span class="pre">app_directories</span></code> template loader works as described above, you can refer to this template within Django simply as <code class="docutils literal"><span class="pre">polls/index.html</span></code>.</p>
<div class="admonition-template-namespacing admonition">
<p class="first admonition-title">Template namespacing</p>
<p class="last">Now we <em>might</em> be able to get away with putting our templates directly in <code class="docutils literal"><span class="pre">polls/templates</span></code> (rather than creating another <code class="docutils literal"><span class="pre">polls</span></code> subdirectory), but it would actually be a bad idea. Django will choose the first template it finds whose name matches, and if you had a template with the same name in a <em>different</em>application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the easiest way to ensure this is by <em>namespacing</em> them. That is, by putting those templates inside <em>another</em> directory named for the application itself.</p>
</div>
<p>Put the following code in that template:</p>
<div class="highlight-html+django">
<div class="snippet-filename">polls/templates/polls/index.html</div>
<div class="highlight">
<pre><span></span><span class="cp">{%</span> <span class="k">if</span> <span class="nv">latest_question_list</span> <span class="cp">%}</span>
    <span class="p">&lt;</span><span class="nt">ul</span><span class="p">&gt;</span>
    <span class="cp">{%</span> <span class="k">for</span> <span class="nv">question</span> <span class="k">in</span> <span class="nv">latest_question_list</span> <span class="cp">%}</span>
        <span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">"/polls/</span><span class="cp">{{</span> <span class="nv">question.id</span> <span class="cp">}}</span><span class="s">/"</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
    <span class="cp">{%</span> <span class="k">endfor</span> <span class="cp">%}</span>
    <span class="p">&lt;/</span><span class="nt">ul</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">else</span> <span class="cp">%}</span>
    <span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>No polls are available.<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">endif</span> <span class="cp">%}</span>
</pre>
</div>
</div>
<p>Now let’s update our <code class="docutils literal"><span class="pre">index</span></code> view in <code class="docutils literal"><span class="pre">polls/views.py</span></code> to use the template:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/views.py</div>
<div class="highlight">
<pre><span></span><span class="kn">from</span> <span class="nn">django.http</span> <span class="k">import</span> <span class="n">HttpResponse</span>
<span class="kn">from</span> <span class="nn">django.template</span> <span class="k">import</span> <span class="n">loader</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>


<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="n">latest_question_list</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">'-pub_date'</span><span class="p">)[:</span><span class="mi">5</span><span class="p">]</span>
    <span class="n">template</span> <span class="o">=</span> <span class="n">loader</span><span class="o">.</span><span class="n">get_template</span><span class="p">(</span><span class="s1">'polls/index.html'</span><span class="p">)</span>
    <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'latest_question_list'</span><span class="p">:</span> <span class="n">latest_question_list</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="n">template</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">request</span><span class="p">))</span>
</pre>
</div>
</div>
<p>That code loads the template called <code class="docutils literal"><span class="pre">polls/index.html</span></code> and passes it a context. The context is a dictionary mapping template variable names to Python objects.</p>
<p>Load the page by pointing your browser at “/polls/”, and you should see a bulleted-list containing the “What’s up” question from <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial02/"><span class="doc">Tutorial 2</span></a>. The link points to the question’s detail page.</p>
<div class="section" id="s-a-shortcut-render"><span id="a-shortcut-render"></span>
<h3>A shortcut: <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.render" title="django.shortcuts.render"><code class="xref py py-func docutils literal"><span class="pre">render()</span></code></a><a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-render" title="Permalink to this headline">¶</a></h3>
<p>It’s a very common idiom to load a template, fill a context and return an <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a> object with the result of the rendered template. Django provides a shortcut. Here’s the full <code class="docutils literal"><span class="pre">index()</span></code> view, rewritten:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/views.py</div>
<div class="highlight">
<pre><span></span><span class="kn">from</span> <span class="nn">django.shortcuts</span> <span class="k">import</span> <span class="n">render</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>


<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="n">latest_question_list</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">'-pub_date'</span><span class="p">)[:</span><span class="mi">5</span><span class="p">]</span>
    <span class="n">context</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'latest_question_list'</span><span class="p">:</span> <span class="n">latest_question_list</span><span class="p">}</span>
    <span class="k">return</span> <span class="n">render</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="s1">'polls/index.html'</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span>
</pre>
</div>
</div>
<p>Note that once we’ve done this in all these views, we no longer need to import <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/templates/#module-django.template.loader" title="django.template.loader"><code class="xref py py-mod docutils literal"><span class="pre">loader</span></code></a> and <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a> (you’ll want to keep <code class="docutils literal"><span class="pre">HttpResponse</span></code> if you still have the stub methods for <code class="docutils literal"><span class="pre">detail</span></code>, <code class="docutils literal"><span class="pre">results</span></code>, and <code class="docutils literal"><span class="pre">vote</span></code>).</p>
<p>The <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.render" title="django.shortcuts.render"><code class="xref py py-func docutils literal"><span class="pre">render()</span></code></a> function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a> object of the given template rendered with the given context.</p>
</div>
</div>
<div class="section" id="s-raising-a-404-error"><span id="raising-a-404-error"></span>
<h2>Raising a 404 error<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#raising-a-404-error" title="Permalink to this headline">¶</a></h2>
<p>Now, let’s tackle the question detail view – the page that displays the question text for a given poll. Here’s the view:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/views.py</div>
<div class="highlight">
<pre><span></span><span class="kn">from</span> <span class="nn">django.http</span> <span class="k">import</span> <span class="n">Http404</span>
<span class="kn">from</span> <span class="nn">django.shortcuts</span> <span class="k">import</span> <span class="n">render</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>
<span class="c1"># ...</span>
<span class="k">def</span> <span class="nf">detail</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">question</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">pk</span><span class="o">=</span><span class="n">question_id</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">Question</span><span class="o">.</span><span class="n">DoesNotExist</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">Http404</span><span class="p">(</span><span class="s2">"Question does not exist"</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">render</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="s1">'polls/detail.html'</span><span class="p">,</span> <span class="p">{</span><span class="s1">'question'</span><span class="p">:</span> <span class="n">question</span><span class="p">})</span>
</pre>
</div>
</div>
<p>The new concept here: The view raises the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> exception if a question with the requested ID doesn’t exist.</p>
<p>We’ll discuss what you could put in that <code class="docutils literal"><span class="pre">polls/detail.html</span></code> template a bit later, but if you’d like to quickly get the above example working, a file containing just:</p>
<div class="highlight-html+django">
<div class="snippet-filename">polls/templates/polls/detail.html</div>
<div class="highlight">
<pre><span></span><span class="cp">{{</span> <span class="nv">question</span> <span class="cp">}}</span>
</pre>
</div>
</div>
<p>will get you started for now.</p>
<div class="section" id="s-a-shortcut-get-object-or-404"><span id="a-shortcut-get-object-or-404"></span>
<h3>A shortcut: <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a><a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-get-object-or-404" title="Permalink to this headline">¶</a></h3>
<p>It’s a very common idiom to use <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/models/querysets/#django.db.models.query.QuerySet.get" title="django.db.models.query.QuerySet.get"><code class="xref py py-meth docutils literal"><span class="pre">get()</span></code></a> and raise <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> if the object doesn’t exist. Django provides a shortcut. Here’s the <code class="docutils literal"><span class="pre">detail()</span></code> view, rewritten:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/views.py</div>
<div class="highlight">
<pre><span></span><span class="kn">from</span> <span class="nn">django.shortcuts</span> <span class="k">import</span> <span class="n">get_object_or_404</span><span class="p">,</span> <span class="n">render</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>
<span class="c1"># ...</span>
<span class="k">def</span> <span class="nf">detail</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="n">question</span> <span class="o">=</span> <span class="n">get_object_or_404</span><span class="p">(</span><span class="n">Question</span><span class="p">,</span> <span class="n">pk</span><span class="o">=</span><span class="n">question_id</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">render</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="s1">'polls/detail.html'</span><span class="p">,</span> <span class="p">{</span><span class="s1">'question'</span><span class="p">:</span> <span class="n">question</span><span class="p">})</span>
</pre>
</div>
</div>
<p>The <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a> function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/models/querysets/#django.db.models.query.QuerySet.get" title="django.db.models.query.QuerySet.get"><code class="xref py py-meth docutils literal"><span class="pre">get()</span></code></a> function of the model’s manager. It raises <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> if the object doesn’t exist.</p>
<div class="admonition-philosophy admonition">
<p class="first admonition-title">Philosophy</p>
<p>Why do we use a helper function <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a> instead of automatically catching the<a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist" title="django.core.exceptions.ObjectDoesNotExist"><code class="xref py py-exc docutils literal"><span class="pre">ObjectDoesNotExist</span></code></a> exceptions at a higher level, or having the model API raise <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> instead of<a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist" title="django.core.exceptions.ObjectDoesNotExist"><code class="xref py py-exc docutils literal"><span class="pre">ObjectDoesNotExist</span></code></a>?</p>
<p class="last">Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#module-django.shortcuts" title="django.shortcuts: Convenience shortcuts that span multiple levels of Django's MVC stack."><code class="xref py py-mod docutils literal"><span class="pre">django.shortcuts</span></code></a> module.</p>
</div>
<p>There’s also a <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.get_list_or_404" title="django.shortcuts.get_list_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_list_or_404()</span></code></a> function, which works just as <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a> – except using <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/models/querysets/#django.db.models.query.QuerySet.filter" title="django.db.models.query.QuerySet.filter"><code class="xref py py-meth docutils literal"><span class="pre">filter()</span></code></a>instead of <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/models/querysets/#django.db.models.query.QuerySet.get" title="django.db.models.query.QuerySet.get"><code class="xref py py-meth docutils literal"><span class="pre">get()</span></code></a>. It raises <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> if the list is empty.</p>
</div>
</div>
<div class="section" id="s-use-the-template-system"><span id="use-the-template-system"></span>
<h2>Use the template system<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#use-the-template-system" title="Permalink to this headline">¶</a></h2>
<p>Back to the <code class="docutils literal"><span class="pre">detail()</span></code> view for our poll application. Given the context variable <code class="docutils literal"><span class="pre">question</span></code>, here’s what the <code class="docutils literal"><span class="pre">polls/detail.html</span></code> template might look like:</p>
<div class="highlight-html+django">
<div class="snippet-filename">polls/templates/polls/detail.html</div>
<div class="highlight">
<pre><span></span><span class="p">&lt;</span><span class="nt">h1</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">h1</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">ul</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">for</span> <span class="nv">choice</span> <span class="k">in</span> <span class="nv">question.choice_set.all</span> <span class="cp">%}</span>
    <span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">choice.choice_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">endfor</span> <span class="cp">%}</span>
<span class="p">&lt;/</span><span class="nt">ul</span><span class="p">&gt;</span>
</pre>
</div>
</div>
<p>The template system uses dot-lookup syntax to access variable attributes. In the example of <code class="docutils literal"><span class="pre">{{</span><span class="pre">question.question_text</span> <span class="pre">}}</span></code>, first Django does a dictionary lookup on the object <code class="docutils literal"><span class="pre">question</span></code>. Failing that, it tries an attribute lookup – which works, in this case. If attribute lookup had failed, it would’ve tried a list-index lookup.</p>
<p>Method-calling happens in the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#std:templatetag-for"><code class="xref std std-ttag docutils literal"><span class="pre">{%</span> <span class="pre">for</span> <span class="pre">%}</span></code></a> loop: <code class="docutils literal"><span class="pre">question.choice_set.all</span></code> is interpreted as the Python code<code class="docutils literal"><span class="pre">question.choice_set.all()</span></code>, which returns an iterable of <code class="docutils literal"><span class="pre">Choice</span></code> objects and is suitable for use in the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#std:templatetag-for"><code class="xref std std-ttag docutils literal"><span class="pre">{%</span> <span class="pre">for</span> <span class="pre">%}</span></code></a>tag.</p>
<p>See the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/topics/templates/"><span class="doc">template guide</span></a> for more about templates.</p>
</div>
<div class="section" id="s-removing-hardcoded-urls-in-templates"><span id="removing-hardcoded-urls-in-templates"></span>
<h2>Removing hardcoded URLs in templates<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#removing-hardcoded-urls-in-templates" title="Permalink to this headline">¶</a></h2>
<p>Remember, when we wrote the link to a question in the <code class="docutils literal"><span class="pre">polls/index.html</span></code> template, the link was partially hardcoded like this:</p>
<div class="highlight-html+django">
<div class="highlight">
<pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">"/polls/</span><span class="cp">{{</span> <span class="nv">question.id</span> <span class="cp">}}</span><span class="s">/"</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre>
</div>
</div>
<p>The problem with this hardcoded, tightly-coupled approach is that it becomes challenging to change URLs on projects with a lot of templates. However, since you defined the name argument in the <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/ref/urls/#django.conf.urls.url" title="django.conf.urls.url"><code class="xref py py-func docutils literal"><span class="pre">url()</span></code></a> functions in the <code class="docutils literal"><span class="pre">polls.urls</span></code> module, you can remove a reliance on specific URL paths defined in your url configurations by using the <code class="docutils literal"><span class="pre">{%</span> <span class="pre">url</span> <span class="pre">%}</span></code> template tag:</p>
<div class="highlight-html+django">
<div class="highlight">
<pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">"</span><span class="cp">{%</span> <span class="k">url</span> <span class="s1">'detail'</span> <span class="nv">question.id</span> <span class="cp">%}</span><span class="s">"</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre>
</div>
</div>
<p>The way this works is by looking up the URL definition as specified in the <code class="docutils literal"><span class="pre">polls.urls</span></code> module. You can see exactly where the URL name of ‘detail’ is defined below:</p>
<div class="highlight-default">
<div class="highlight">
<pre><span></span><span class="o">...</span>
<span class="c1"># the 'name' value as called by the {% url %} template tag</span>
<span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^(?P&lt;question_id&gt;[0-9]+)/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'detail'</span><span class="p">),</span>
<span class="o">...</span>
</pre>
</div>
</div>
<p>If you want to change the URL of the polls detail view to something else, perhaps to something like <code class="docutils literal"><span class="pre">polls/specifics/12/</span></code> instead of doing it in the template (or templates) you would change it in <code class="docutils literal"><span class="pre">polls/urls.py</span></code>:</p>
<div class="highlight-default">
<div class="highlight">
<pre><span></span><span class="o">...</span>
<span class="c1"># added the word 'specifics'</span>
<span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^specifics/(?P&lt;question_id&gt;[0-9]+)/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'detail'</span><span class="p">),</span>
<span class="o">...</span>
</pre>
</div>
</div>
</div>
<div class="section" id="s-namespacing-url-names"><span id="namespacing-url-names"></span>
<h2>Namespacing URL names<a class="headerlink" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#namespacing-url-names" title="Permalink to this headline">¶</a></h2>
<p>The tutorial project has just one app, <code class="docutils literal"><span class="pre">polls</span></code>. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the <code class="docutils literal"><span class="pre">polls</span></code> app has a <code class="docutils literal"><span class="pre">detail</span></code> view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the <code class="docutils literal"><span class="pre">{%</span> <span class="pre">url</span> <span class="pre">%}</span></code> template tag?</p>
<p>The answer is to add namespaces to your URLconf. In the <code class="docutils literal"><span class="pre">polls/urls.py</span></code> file, go ahead and add an <code class="docutils literal"><span class="pre">app_name</span></code> to set the application namespace:</p>
<div class="highlight-default">
<div class="snippet-filename">polls/urls.py</div>
<div class="highlight">
<pre><span></span><span class="kn">from</span> <span class="nn">django.conf.urls</span> <span class="k">import</span> <span class="n">url</span>

<span class="kn">from</span> <span class="nn">.</span> <span class="k">import</span> <span class="n">views</span>

<span class="n">app_name</span> <span class="o">=</span> <span class="s1">'polls'</span>
<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'index'</span><span class="p">),</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^(?P&lt;question_id&gt;[0-9]+)/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'detail'</span><span class="p">),</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^(?P&lt;question_id&gt;[0-9]+)/results/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">results</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'results'</span><span class="p">),</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">'^(?P&lt;question_id&gt;[0-9]+)/vote/$'</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">vote</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'vote'</span><span class="p">),</span>
<span class="p">]</span>
</pre>
</div>
</div>
<p>Now change your <code class="docutils literal"><span class="pre">polls/index.html</span></code> template from:</p>
<div class="highlight-html+django">
<div class="snippet-filename">polls/templates/polls/index.html</div>
<div class="highlight">
<pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">"</span><span class="cp">{%</span> <span class="k">url</span> <span class="s1">'detail'</span> <span class="nv">question.id</span> <span class="cp">%}</span><span class="s">"</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre>
</div>
</div>
<p>to point at the namespaced detail view:</p>
<div class="highlight-html+django">
<div class="snippet-filename">polls/templates/polls/index.html</div>
<div class="highlight">
<pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">"</span><span class="cp">{%</span> <span class="k">url</span> <span class="s1">'polls:detail'</span> <span class="nv">question.id</span> <span class="cp">%}</span><span class="s">"</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre>
</div>
</div>
<p>When you’re comfortable with writing views, read <a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial04/"><span class="doc">part 4 of this tutorial</span></a> to learn about simple form processing and generic views.</p>
</div>
</div>
</div>
<div class="browse-horizontal">
<div class="left"><a href="https://docs.djangoproject.com/en/1.10/intro/tutorial02/"><i class="icon icon-chevron-left"></i> Writing your first Django app, part 2</a></div>
<div class="right"><a href="https://docs.djangoproject.com/en/1.10/intro/tutorial04/">Writing your first Django app, part 4 <i class="icon icon-chevron-right"></i></a></div>
</div>
</div>
<h1 class="visuallyhidden">Additional Information</h1>
<div><form action="https://docs.djangoproject.com/en/1.10/search/" class="search form-input"><label class="visuallyhidden" for="news-search">Search:</label><input id="id_q" name="q" type="search"><button type="submit"><i class="icon icon-search"></i><span class="visuallyhidden">搜索</span></button></form>
<div class="fundraising-sidebar">
<h2>Support Django!</h2>
<div class="small-heart"><img alt="Support Django!" src="https://docs.djangoproject.com/s/img/small-fundraising-heart.d255f6e934e5.png"></div>
<div class="small-cta">
<ul class="list-links-small">
<li><a href="https://www.djangoproject.com/fundraising/">Adon Metcalfe donated to the Django Software Foundation to support Django development. Donate today!</a></li>
</ul>
</div>
</div>
<h2>Contents</h2>
<ul>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#">Writing your first Django app, part 3</a>
<ul>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#overview">Overview</a></li>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#writing-more-views">Writing more views</a></li>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#write-views-that-actually-do-something">Write views that actually do something</a>
<ul>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-render">A shortcut: <code class="docutils literal"><span class="pre">render()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#raising-a-404-error">Raising a 404 error</a>
<ul>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-get-object-or-404">A shortcut: <code class="docutils literal"><span class="pre">get_object_or_404()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#use-the-template-system">Use the template system</a></li>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#removing-hardcoded-urls-in-templates">Removing hardcoded URLs in templates</a></li>
<li><a class="reference internal" href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/#namespacing-url-names">Namespacing URL names</a></li>
</ul>
</li>
</ul>
<h2>Browse</h2>
<ul>
<li>Prev: <a href="https://docs.djangoproject.com/en/1.10/intro/tutorial02/">Writing your first Django app, part 2</a></li>
<li>Next: <a href="https://docs.djangoproject.com/en/1.10/intro/tutorial04/">Writing your first Django app, part 4</a></li>
<li><a href="https://docs.djangoproject.com/en/1.10/contents/">Table of contents</a></li>
<li><a href="https://docs.djangoproject.com/en/1.10/genindex/">General Index</a></li>
<li><a href="https://docs.djangoproject.com/en/1.10/py-modindex/">Python Module Index</a></li>
</ul>
<h2>You are here:</h2>
<ul>
<li><a href="https://docs.djangoproject.com/en/1.10/">Django 1.10 documentation</a>
<ul>
<li><a href="https://docs.djangoproject.com/en/1.10/intro/">Getting started</a>
<ul>
<li>Writing your first Django app, part 3</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="getting-help-sidebar">Getting help</h2>
<dl class="list-links">
<dt><a href="https://docs.djangoproject.com/en/1.10/faq/">FAQ</a></dt>
<dd>Try the FAQ — it's got answers to many common questions.</dd>
<dt><a href="https://docs.djangoproject.com/en/stable/genindex/">Index</a>, <a href="https://docs.djangoproject.com/en/stable/py-modindex/">Module Index</a>, or <a href="https://docs.djangoproject.com/en/stable/contents/">Table of Contents</a></dt>
<dd>Handy when looking for specific information.</dd>
<dt><a href="http://groups.google.com/group/django-users/">django-users mailing list</a></dt>
<dd>Search for information in the archives of the django-users mailing list, or post a question.</dd>
<dt><a>#django IRC channel</a></dt>
<dd>Ask a question in the #django IRC channel, or search the IRC logs to see if it’s been asked before.</dd>
<dt><a href="http://code.djangoproject.com/">Ticket tracker</a></dt>
<dd>Report bugs with Django or Django documentation in our ticket tracker.</dd>
</dl>
<h2>Download:</h2>
<p>Offline (Django 1.10): <a href="https://docs.djangoproject.com/m/docs/django-docs-1.10-en.zip">HTML</a> | <a href="https://media.readthedocs.org/pdf/django/1.10.x/django.pdf">PDF</a> | <a href="https://media.readthedocs.org/epub/django/1.10.x/django.epub">ePub</a> <br><span class="quiet">Provided by <a href="https://readthedocs.org/">Read the Docs</a>.</span></p>
</div>
</div>
<div>
<div class="subfooter">
<div class="container">
<h1 class="visuallyhidden">Django Links</h1>
<div class="col learn">
<h2>Learn More</h2>
<ul>
<li><a href="https://www.djangoproject.com/start/overview/">About Django</a></li>
<li><a href="https://www.djangoproject.com/start/">Getting Started with Django</a></li>
<li><a href="https://docs.djangoproject.com/en/dev/internals/organization/">Team Organization</a></li>
<li><a href="https://www.djangoproject.com/foundation/">Django Software Foundation</a></li>
<li><a href="https://www.djangoproject.com/conduct/">Code of Conduct</a></li>
<li><a href="https://www.djangoproject.com/diversity/">Diversity statement</a></li>
</ul>
</div>
<div class="col involved">
<h2>Get Involved</h2>
<ul>
<li><a href="https://www.djangoproject.com/community/">Join a Group</a></li>
<li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/">Contribute to Django</a></li>
<li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/">Submit a Bug</a></li>
<li><a href="https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues">Report a Security Issue</a></li>
</ul>
</div>
<div class="col follow last-child">
<h2>Follow Us</h2>
<ul>
<li><a href="https://github.com/django">GitHub</a></li>
<li><a href="https://twitter.com/djangoproject">Twitter</a></li>
<li><a href="https://www.djangoproject.com/rss/weblog/">News RSS</a></li>
<li><a href="https://groups.google.com/forum/#!forum/django-users">Django Users Mailing List</a></li>
</ul>
</div>
</div>
</div>
<div class="footer">
<div class="container">
<div class="footer-logo"><a class="logo" href="https://www.djangoproject.com/">Django</a></div>
<ul class="thanks">
<li><span>Hosting by</span><a class="rackspace" href="http://rackspace.com/">Rackspace</a><span>Search by</span><a class="elastic" href="https://www.elastic.co/">Elastic Search</a></li>
<li class="design"><span>Design by</span><a class="threespot" href="http://www.threespot.com/">Threespot</a> <span class="ampersand">&amp;</span> <a class="andrevv" href="http://andrevv.com/"></a></li>
</ul>
<p class="copyright">© 2005-2017 <a href="https://www.djangoproject.com/foundation/">Django Software Foundation</a> and individual contributors. Django is a <a href="https://www.djangoproject.com/trademarks/">registered trademark</a> of the Django Software Foundation.</p>
</div>
</div>
</div>'''}


paper = Paper(**all_kwargs)
paper.category = Category.objects.get(name=u'技术前沿')
paper.save()

user_kwargs = {"username": u"泛资讯收割者",
                  "email": u"shikanon@foxmail.com",
                  "is_staff": True,
                  "is_active": True,}
user = User(**user_kwargs)
user.set_password('new password')
user = User.objects.get(username=u"泛资讯收割者")
user.citizen.nickname = u"资讯收割者1号"
user.citizen.is_gril = False
user.save()
# citizen_kwargs = {"nickname": u"资讯收割者1号","is_gril": False}
# people = Citizen(**citizen_kwargs)
# people.user = user
# people.save()