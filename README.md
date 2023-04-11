# AI and Business Rules for Excel Power Users

<a href="https://www.packtpub.com/product/ai-and-business-rule-engines-for-excel-power-users/9781804619544"><img src="https://m.media-amazon.com/images/I/511zmj7OcXL._SX403_BO1,204,203,200_.jpg" alt="AI and Business Rules for Excel Power Users" height="256px" align="right"></a>

This is the code repository for [AI and Business Rules for Excel Power Users](https://www.packtpub.com/product/ai-and-business-rule-engines-for-excel-power-users/9781804619544), published by Packt.

**Capture and scale your business knowledge into the cloud – with Microsoft 365, Decision Models, and AI tools from IBM and Red Hat**

## What is this book about?
Microsoft Excel is widely adopted across diverse industries, but Excel Power Users often encounter limitations such as complex formulas, obscure business knowledge, and errors from using outdated sheets. They need a better enterprise-level solution, and this book introduces Business rules combined with the power of AI to tackle the limitations of Excel.

This book covers the following exciting features:
* Use KIE and Drools decision services to write AI-based business rules
* Link Business Rules to Excel using Power Query, Script Lab, Office Script, and VBA
* Build an end-to-end workflow with Microsoft Power Automate and Forms while integrating it with Excel and Kogito
* Collaborate on and deploy your decision models using OpenShift, Azure, and GitHub
* Discover advanced editing using the graphical Decision Model Notation (DMN) and testing tools
* Use Kogito to combine AI solutions with Excel

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/180461954X) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter06.

The code will look like the following:
```
let
 // "SourceUrl" with quotes needs to match the named range on 
our Excel sheet. You may need to change {1} to {0} depending on 
when your first line begins
 pSourceUrl = Excel.CurrentWorkbook(){[Name="SourceUrl"]}
[Content]{1}[Column1]
in
 pSourceUrl
```

**Following is what you need for this book:**
This book is for Excel power users, business users, and business analysts looking for a tool to capture their knowledge and deploy it as part of enterprise-grade systems. Working proficiency with MS Excel is required. Basic knowledge of web technologies and scripting would be an added advantage

With the following software and hardware list you can run all code files present in the book (Chapter 1-12).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 6-8 | Microsoft Excel and Office 365 | Windows, Mac OS X, and Linux (Any) |
| 10 | Docker | Windows, Mac OS X, and Linux (Any) |
| Appendix A | Visual Basic for Applications | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/EAEVJ).

### Related products
* Exploring Microsoft Excel’s Hidden Treasures [[Packt]](https://www.packtpub.com/product/exploring-microsoft-excels-hidden-treasures/9781803243948?utm_source=github&utm_medium=repository&utm_campaign=9781803243948) [[Amazon]](https://www.amazon.com/dp/1803243945)

* VBA Automation for Excel 2019 Cookbook [[Packt]](https://subscription.packtpub.com/search?query=9781789610031&utm_source=github&utm_medium=repository&utm_campaign=9781803242002) [[Amazon]](https://www.amazon.com/dp/1789610036)


## Get to Know the Author
**Paul Browne**
is a Programme Manager - Training and Consulting at Enterprise Ireland. His skillset includes delivering consulting and training into companies to help them grow faster, better and earlier. Particular focus in working on Digital Transformation alongside Sales and Marketing, Manufacturing and Financial teams. His educational qualifications includes Msc Advanced Software Engineering at University College Dublin and BA European Business Studies with French at Ulster University, Northern Ireland. His professional qualifications includes ACCA (Financial management modules), CIPS - Procurement Professional, and Technical certifications from Oracle (Java) and Microsoft.

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781804619544">https://packt.link/free-ebook/9781804619544 </a> </p>
