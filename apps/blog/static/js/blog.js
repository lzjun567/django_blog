$("#blog-search").click(function(){
    q = $("#blog-query").val()
    g_search(q);
});

$("#blog-query").keydown(function(e){
    if(e.keyCode==13){
        q = $(this).val();
        g_search(q);
    }
});

function g_search(query){
    q = "site:foofish.net/ "+query
    location.href='http://www.google.com.hk/search?q='+q
}
