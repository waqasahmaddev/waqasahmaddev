<a href="https://waqasahmaddev.com">
  <img src="assets/banner.svg" width="100%" alt="GET /waqas 200 OK. Waqas Ahmad, Software Engineer. Builds backend systems, web apps and dev tools. Loves .NET and system design." />
</a>

<p align="center">
  <a href="https://waqasahmaddev.com"><img src="assets/card-site.svg" width="32%" alt="Website: waqasahmaddev.com" /></a>
  <a href="https://waqasahmaddev.com/posts/"><img src="assets/card-posts.svg" width="32%" alt="Writing: waqasahmaddev.com/posts" /></a>
  <a href="mailto:hello@waqasahmaddev.com"><img src="assets/card-contact.svg" width="32%" alt="Contact: hello@waqasahmaddev.com" /></a>
</p>

### Hey, I'm Waqas 👋

I'm a full stack software engineer with 10+ years of experience, mostly in .NET. I build backend systems, web apps and APIs, and I love system design. I also write about system design and AI.

My website is built like an API, so this page is too. Each section below is an endpoint.

### `GET /waqas`

```json
{
  "name": "Waqas Ahmad",
  "role": "Software Engineer",
  "works_with": ["C#", ".NET", "ASP.NET Core", "SQL Server", "PostgreSQL", "JavaScript"],
  "loves": ["system design", ".NET", "small useful tools"],
  "writes_about": ["system design", "AI"],
  "links": {
    "website": "https://waqasahmaddev.com",
    "linkedin": "https://www.linkedin.com/in/waqas-ahmad62"
  }
}
```

### `GET /projects`

Small, focused open-source tools. Fast, light and friendly to the keyboard.

| Project | What it is | Language |
|---|---|---|
| **[snapricot](https://github.com/waqasahmaddev/snapricot)** · [site](https://waqasahmaddev.github.io/snapricot/) | A fast, open-source screenshot tool for Windows | C# |
| **[flow-select](https://github.com/waqasahmaddev/flow-select)** · [site](https://waqasahmaddev.github.io/flow-select/) | A fast, keyboard-first select for plain HTML forms. No dependencies | JavaScript |
| **[flow-datepicker](https://github.com/waqasahmaddev/flow-datepicker)** · [site](https://waqasahmaddev.github.io/flow-datepicker/) | A light, keyboard-first date, time and range picker. No dependencies | JavaScript |
| **[PulseSharp](https://github.com/pulsesharp/pulsesharp)** · [site](https://pulsesharp.github.io/pulsesharp/) | Lightweight, durable events and background jobs for .NET. Preview release | C# |

### `GET /posts?limit=3`

<!-- POSTS:START -->
- **[A static site on Cloudflare for free: the setup I'd repeat](https://waqasahmaddev.com/posts/a-static-site-on-cloudflare-for-free/)**  
  <sub>2026-11-13 · 2 min read</sub>
- **[What ten years of .NET taught me to stop doing](https://waqasahmaddev.com/posts/what-ten-years-of-dotnet-taught-me-to-stop-doing/)**  
  <sub>2026-11-06 · 3 min read</sub>
- **[Why I built PulseSharp instead of using a bigger library](https://waqasahmaddev.com/posts/why-i-built-pulsesharp/)**  
  <sub>2026-10-29 · 3 min read</sub>
<!-- POSTS:END -->

This list updates itself every day from my own API.

### `POST /contact`

Have a role, a project or a hard problem? Send the request: [hello@waqasahmaddev.com](mailto:hello@waqasahmaddev.com) or find me on [LinkedIn](https://www.linkedin.com/in/waqas-ahmad62).

---

<sub>Try it yourself: <code>curl https://waqasahmaddev.com/api/waqas</code></sub>
