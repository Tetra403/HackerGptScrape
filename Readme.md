<h1>🧠 HackerGPT</h1>

<img src="assest\Project Photo.png" width="400" height="200">

<p><strong>HackerGPT</strong> is a Python-based scraping tool designed for ethical hackers, cybersecurity researchers, and developers who need clean and structured access to data from the web.</p>

<p>It’s fast, lightweight, and built with flexibility in mind. Use it to automate recon, gather OSINT, or just extract data that matters.</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>🌐 URL scraping with custom headers & proxy support</li>
  <li>🔍 Regex & DOM-based data filtering</li>
  <li>🧰 Modular codebase for easy customization</li>
  <li>🧪 Ideal for CTFs, bug bounty recon, and data-driven research</li>
  <li>☠️ Anti-bot evasion techniques (randomized User-Agent, delay, etc.)</li>
</ul>

<hr>

<h2>⚙️ Tech Stack</h2>
<ul>
  <li>Python 3.x</li>
  <li><code>requests</code>, <code>beautifulsoup4</code>, <code>lxml</code></li>
  <li>(Optional) <code>Selenium</code> for dynamic pages</li>
  <li>CLI-based interface</li>
</ul>

<hr>

<h2>📦 Installation</h2>
<pre><code>git clone https://github.com/tetra403/HackerGPT.git
cd HackerGPT
pip install -r requirements.txt
</code></pre>

<hr>

<h2>🧪 Usage</h2>
<pre><code>python hackergpt.py --url "https://example.com" --pattern "&lt;title&gt;(.*?)&lt;/title&gt;"
</code></pre>

<p>Or import as a module:</p>

<pre><code>from hackergpt.core import Scraper

scraper = Scraper(url="https://example.com")
data = scraper.extract("//h1")
print(data)
</code></pre>

<hr>

<h2>🔐 Disclaimer</h2>
<p>This tool is for <strong>educational and authorized security testing purposes only</strong>.</p>
<p>Do not use it on targets without <strong>explicit permission</strong>.</p>

<blockquote>
  ❝ Breaking the system is easy. Understanding it is what makes you powerful. ❞
</blockquote>

<hr>

<h2>📎 License</h2>
<p>MIT License – feel free to use, modify, and contribute.</p>

<hr>

<h2>💬 Contact</h2>
<p>Maintained by <a href="https://github.com/tetra403" target="_blank">tetra403</a></p>
<p>Open to contributions, suggestions, or collaborations.</p>
