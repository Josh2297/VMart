// Funtion to Extract CSRF Token From Cookie
function CSRF(){
    var cookies=document.cookie.split(';');r=/csrftoken/i;
    for (c of cookies){
        if (r.test(c)){
            var cookie=c.split('=')[1]  
        }
    }
return cookie
} // End of CSRF Token Function


function IncreaseQuantity(element) {
    var quantity=element;qtyv=parseInt(quantity.value)
    quantity.value=qtyv+1
}
function DecreaseQuantity(element) {
    var quantity=element;qtyv=parseInt(quantity.value)
    if (qtyv>1){
        quantity.value=qtyv-1
    }
    else {quantity.value=1}
}
function addTask(inputoption) {
    var message="<div class=\"d-flex w-75 w-lg-50 mx-auto input-group input-group-sm\" style=\"display:inline-block\" >\
<button class=\"btn btn-primary decrease\" type=\"button\" style=\"font-weight:bold\">-</button>\
<input type=\"text\" class=\"form-control text-center "+inputoption+"\" quantity\" min=\"1\" value=\"1\" name=\"Quantity\" disabled />\
<button class=\"btn btn-primary increase\" type=\"button\" style=\"font-weight:bold\">+</button>\
</div>"
    /* writeIDHTML('testinject',message)
    writeClassHTML(message)
    init()*/
    return message
}
function addCartMessage(product_name,product_price,product_value,product_id,size){
    var cartmessage=("<tr style=\"white-space:nowrap;\"><td style=\"white-space:nowrap;overflow-x:hidden\" >"+product_name+' '+size+"</td><td class=\" \" style=\"display:inline-block\"><div class=\"input-group input-group-sm\" style=\"font-size:90%\">\
            <button class=\"btn btn-primary decrease\" type=\"button\" style=\"font-weight:bold\">-</button><input type=\"text\" class=\"form-control text-center\
             "+product_id+"\" value=\""+product_value+"\" disabled /><button class=\"btn btn-primary increase\" type=\"button\" style=\"font-weight:bold\">+</button></div></td><td class=\"ps-0\" style=\"width:50px;display:inline-block\">"+product_price+"</td>\
            <td style=\"display:inline-block\"><a class=\"text-decoration-none removeitemfromcart\" product=\""+product_id+"\" href=\"#\">Remove</a></td></tr>")
    return cartmessage
        }
// Working Function 
function init1 (){
    localStorage.clear()
    //Persisting Data To Session Storage
   if (sessionStorage!==undefined && sessionStorage.getItem('injectItems')!==null){
        //Persist Cart Items
        let cartid=document.getElementById(sessionStorage.getItem('carttable'))
        let cartmessage=JSON.parse(sessionStorage.getItem('cartitems'))
        cartid.innerHTML=cartmessage[1].join("")
        //Persist Main Content Data
        let sessiondata=JSON.parse(sessionStorage.getItem('injectItems'))
        for (var singledata of sessiondata){
        let cbutton=document.getElementById(singledata.cartbutton)
        if (cbutton!==null){
        let session_message=singledata.message
        cbutton.innerHTML=session_message
        }
        }
    }
    var a=document.body
    a.addEventListener('click',function(event){ 
        if (event.target.className=="badge rounded-pill bg-primary" && event.target.nodeName=='SPAN'){
            var cartbutton=event.target.parentNode.parentNode.parentNode
            /* Cart Item Insert Protocol */
            var productnode=cartbutton.parentNode.children[5] //textContent
            var productid=productnode.id
            var product=productnode.getAttribute('product');
            var size=((productnode.getAttribute('size')!='None') ? productnode.getAttribute('size'):"");
            var price=cartbutton.parentNode.children[2].firstChild.children[1].textContent 
            var message=addTask(productid)
            cartbutton.innerHTML=message
            // Get Cart Table
            var carttable=document.getElementById('carttable')
            //Insert Content Into Cart Table
            carttable.insertAdjacentHTML("beforeEnd",addCartMessage(product,price,1,productid,size))
            // Insert Items into SessionData
            var cartitem={"cartbutton":cartbutton.id,"message":addTask(productid)}
            var cartitems=[[cartbutton.id],[addCartMessage(product,price,1,productid,size)]]
            var cartsession=[cartitem]
            if (sessionStorage.getItem('injectItems')===null){
                sessionStorage.setItem("injectItems",JSON.stringify(cartsession))
                sessionStorage.setItem("carttable",carttable.id)
                sessionStorage.setItem("cartitems",JSON.stringify(cartitems))
            }
            else {
              let tempa=JSON.parse(sessionStorage.getItem('injectItems'));tempa.push(cartitem)
              sessionStorage.setItem("injectItems",JSON.stringify(tempa))
              let temp=JSON.parse(sessionStorage.getItem('cartitems'));
              let temp_id=temp[0];temp_id.push(cartbutton.id);let temp_content=temp[1];temp_content.push(addCartMessage(product,price,1,productid,size))
              sessionStorage.setItem("cartitems",JSON.stringify(temp))
            }
        }
    
    // Listening for Proceed In cart
       
       if (event.target.id=="proceed-cart" && event.target.nodeName=='A'){
        var proceed_cart=document.getElementById('carttable').children;var item_list=[]
        for (item of proceed_cart){
            var temp={'product':item.children[0].textContent,'quantity':item.getElementsByTagName('input')[0].value,'unit_price':item.children[2].textContent};
            temp['price']=parseInt(temp['quantity'])*parseInt(temp['unit_price'])
            item_list.push(temp)
        }
        var csrftoken=CSRF();
    // AJAX 
    var url="/orders/ajax/"
    fetch(url,{
        method:'POST',
        credentials:'same-origin',
        headers: {
            'Accept':'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'item_data':item_list})})
        .then(function(response){
        return response.json()})
        .then(function(txn_id){
            proceed_button=document.getElementById('proceed-cart')
            document.location.href=('/orders/checkout/'+txn_id['data']+'/')
}) }
},false)
    
    // Listening for Increase or Decrease
    a.addEventListener('click',function(event){
        // Increase Button
        if (event.target.className=="btn btn-primary increase" && event.target.nodeName=="BUTTON"){
            let increase=event.target.previousSibling;let qtyClassName=increase.className
            let productUpdate=document.getElementsByClassName(qtyClassName)
            for (let qtyUpdate of productUpdate) {
                IncreaseQuantity(qtyUpdate)
            }
        }
        if (event.target.className=="btn btn-primary decrease" && event.target.nodeName=="BUTTON"){
            let decrease=event.target.nextSibling;let qtyClassName=decrease.className
            let productUpdate=document.getElementsByClassName(qtyClassName)
            for (let qtyUpdate of productUpdate) {
                DecreaseQuantity(qtyUpdate)
            }
        }
    })
    // Clear Cart
    a.addEventListener('click',function(event){
        if (event.target.id=='clear cart' && event.target.nodeName=='BUTTON'){
            sessionStorage.clear()
            document.location.reload(true)
        }
    })
    // Event Listener to Remove Item from Cart
    a.addEventListener('click',function(event){
        if (event.target.className=="text-decoration-none removeitemfromcart" && event.target.nodeName=='A') {
           let removeitem=event.target // Remove Button
           remove_product_name=removeitem.getAttribute('product')
           let local_item_index=JSON.parse(sessionStorage.getItem('cartitems'));let item_index=Number(local_item_index[0].indexOf(remove_product_name))
           // Remove Items From Storage
            itemparent=event.target.parentNode.parentNode
            // Remove Targeted Item from DOM
            let remove_tempa=JSON.parse(sessionStorage.getItem('injectItems'));remove_tempa.splice([item_index],1)
            local_item_index[0].splice([item_index],1);local_item_index[1].splice([item_index],1)
            // Updating The values in session
            sessionStorage.setItem('injectItems',JSON.stringify(remove_tempa));sessionStorage.setItem('cartitems',JSON.stringify(local_item_index))
            // Removing Targeted Item From Main Path
            item=document.getElementById(removeitem.getAttribute('product'))
            if (item!==null){
            let message="<div class=\"d-flex w-50 mx-auto mb-0\"><a class=\"card-link buttoninject\"  href=\"#1\"><span class=\"badge rounded-pill bg-primary\">Add to Cart</span></a></div>"
            item.innerHTML=message;
            }
            itemparent.remove()
        }
    })
}

window.addEventListener('load',init1)