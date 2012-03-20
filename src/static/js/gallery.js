 $(document).ready(function(){
    $("a.colorbox").colorbox({ 
        opacity:0.9 , 
        rel:'group1',
        slideshow:true,
        next:'další',
        close:'zavřít',
        current: "obrázek {current} z {total}",
        width: "80%",
        transition: "elastic",
        slideshowStop: "zastavit prezentaci",
        slideshowStart: "spustit prezentaci",
    });
 });
