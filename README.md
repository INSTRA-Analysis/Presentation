# Presentation

## Dynamic Analysis Overview

This repository contains a comprehensive presentation about dynamic program analysis.

### 📊 Presentation Files

- **[dynamic-analysis-overview.md](dynamic-analysis-overview.md)** - Main presentation file (36 slides)
- **[PRESENTATION-GUIDE.md](PRESENTATION-GUIDE.md)** - Complete guide for presenters and users
- **[RESOURCES.md](RESOURCES.md)** - Comprehensive resource list with tools, books, and links

### 📚 Content Overview

The presentation covers:

1. **Introduction to Dynamic Analysis** - Understanding the fundamentals
2. **What is Dynamic Analysis?** - Definition and key characteristics
3. **Types of Dynamic Analysis** - Profiling, debugging, testing, monitoring, security analysis
4. **Tools and Techniques** - Popular tools and instrumentation methods
5. **Advantages and Disadvantages** - When to use dynamic analysis
6. **Use Cases and Applications** - Real-world scenarios
7. **Comparison with Static Analysis** - Understanding the differences
8. **Best Practices** - How to effectively use dynamic analysis
9. **Real-World Examples** - Memory leak detection and performance optimization cases

### 🎯 Target Audience

- Software developers
- Security analysts
- QA engineers
- DevOps professionals
- Students learning about software analysis

### 🛠️ How to View the Presentation

#### Option 1: View on GitHub (Simplest)
Simply open `dynamic-analysis-overview.md` in GitHub's web interface.

#### Option 2: Convert to Slides with Reveal.js

1. Install reveal-md:
```bash
npm install -g reveal-md
```

2. View the presentation:
```bash
reveal-md dynamic-analysis-overview.md
```

3. Export to HTML:
```bash
reveal-md dynamic-analysis-overview.md --static
```

#### Option 3: Use Marp

1. Install Marp CLI:
```bash
npm install -g @marp-team/marp-cli
```

2. Convert to HTML slides:
```bash
marp dynamic-analysis-overview.md
```

3. Convert to PDF:
```bash
marp dynamic-analysis-overview.md --pdf
```

#### Option 4: Convert with Pandoc

```bash
pandoc dynamic-analysis-overview.md -o dynamic-analysis-overview.pdf
pandoc dynamic-analysis-overview.md -o dynamic-analysis-overview.pptx
```

### 📖 Reading the Presentation

The presentation is formatted with:
- `---` separating slides
- `#` for main titles
- `##` for section headings
- `###` for subsections

Each `---` delimiter indicates a new slide when using presentation tools.

### 🤝 Contributing

Feel free to:
- Suggest improvements
- Add examples
- Correct errors
- Enhance content

### 📝 License

This presentation is part of the INSTRA-Analysis project.

---

**Made with ❤️ by the INSTRA-Analysis team**