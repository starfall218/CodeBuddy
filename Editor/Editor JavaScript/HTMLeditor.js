
  const run = () => {
    let htmlCode = document.getElementById("html-code").value;
    let cssCode = document.getElementById("css-code").value;
    let jsCode = document.getElementById("js-code").value;  
    let output = document.getElementById("run");

    output.contentDocument.body.innerHTML = htmlCode + "<style>" + cssCode +"</style>";
    output.contentWindow.eval(jsCode)
  }
  
 
  
