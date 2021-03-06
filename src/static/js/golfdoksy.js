$('document').ready(function() {
    header_height = 46;
    
    //$.localScroll();
    var scrolls, paddings,
        els = $("#logo, #menu a, p.back a"),
        marker = $("#marker");
    $(window).scroll(function(){
        var scroll = $(this).scrollTop();
        for(var i in scrolls){
            if ( scrolls[i] > scroll-100 ) break;
        }
        marker.css({left: paddings[i]+"px"});
        els.removeClass("active").eq(i).addClass("active");
    }); 

    $(window).resize(function(){
        scrolls = [], paddings = [];
        els.each(function(i){
            paddings.push( $(this).offset().left + $(this).width()/2 + (i==0 ? -16 : 0) );
            var id = $(this).attr("href");
            scrolls.push( $(id).offset().top + header_height);
        });
        scrolls[1] = scrolls[1] + 200;
        $(window).trigger("scroll");
    }).trigger("resize");

    els.click(function(e){
        e.preventDefault();
        var id = $(this).attr("href");
        $('html,body').addClass("scrolling").animate({
            scrollTop: $(id).offset().top - header_height + "px"
        },1000).removeClass("scrolling");
        return false;
    }); 

    $('a.moreinfo').click(function(event){
        var lessDiv = $(this).parent('div.lessinfo');
        var moreDiv = lessDiv.next();
        lessDiv.slideUp();
        moreDiv.slideDown("slow");
        event.preventDefault();
    });
    $('a.lessinfo').click(function(event){
        var moreDiv = $(this).parent('div.moreinfo');
        var lessDiv = moreDiv.prev();
        moreDiv.slideUp();
        lessDiv.slideDown("slow");
        event.preventDefault();
    });
});
