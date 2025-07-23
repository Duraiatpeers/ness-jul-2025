Day1:

1. Recap of Selenium
2. Advanced locators (XPath, CSS), Dynamic locators
3. Extracting Data from Web Tables
4. Synchronization

Selenium
  - Opensource
  - Web Automation
  - Current version is 4.x
  - Supports multiple browsers
  - Supports multiple languages
  - WebDriver protocol

  - WebDriver
       - Web Automation standard set by W3C

  - IDE
     - record and playback


WebDriver
    - get
        - to navigate to an application/url
    - navigate
        - to perform browser functions like refresh, back, forward
    - close / quit
    - find element(s)

WebElement
    Elements
        - Textfield
        - Button
        - links
        - dropdowns
    Actions
        - click
        - send keys
        - clear
        - submit

Locators
   - id
   - name
   - class name
   - link text
   - partial link text
   - tagname
   - xpath
       - absolute xpath
            - /html
       - relative xpath
            - //div/div/h1
       - xpath axes
   - css
      - css selector

Relative locators
   - below
   - above
   - to left of
   - to right of

Synchronization
   - time.sleep
   - Implicit wait
   - Explicit wait
   - Fluent wait


   //form/div[1]/div/div/input - this will break if one more level introduced before input tag
   //form/div[1]//input

   div
    form
      div
       div
         div
           div
             input
      div
       div
        div
          input
