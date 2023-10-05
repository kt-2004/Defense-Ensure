function load(params) {
   const arr = document.getElementsByTagName('section');
   for (let index = 0; index < arr.length; index++) {
      const element = arr[index];
      element.style.display = 'none';
   }


   if (params != "skills") {
      document.getElementById(params).style.display = "flex";
   }
   else {
      document.getElementById(params).style.display = "block";
   }
}