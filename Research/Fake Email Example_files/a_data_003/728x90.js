var tagWidth = 728;
var tagHeight = 90;

var bids = [{"bidder":"districtmDMX","params":{"id":"464425"}}, {"bidder":"fidelity","params":{"zoneid":"48781"}}, {"bidder":"oftmedia","params":{"placementId":"12803051"}}];

var bidTimeOut = 3000;

if (window != window.top) {
   var kadpageurl = document.referrer;
} else {
    var kadpageurl = window.location.href;
}
if (kadpageurl == '') {
    kadpageurl = "fakemailgenerator.com";
}

var passbackTagHtml = "<scr" + "ipt type='text/javascript'> var iframe = 0; var url = document.location.href; if(!window.psa) var psa=0; if(!window.nofill){ var nofill=0; } var src = 0; if(window.top !== window.self){ iframe = 1; src = document.referrer ? encodeURIComponent(document.referrer) : \'BlankRefServe\'; } if(typeof setMIframe !== \'undefined\'){ iframe = setMIframe; } if(typeof setMRefURL !== \'undefined\'){ if(iframe == 1){ src = setMRefURL; }else{ url = setMRefURL; } } if(typeof nonPixel == \'undefined\'){ document.write(\"<img src=\'//pixel.madadsmedia.com/?site=17612&pub=46194&size=20&nofill=\"+nofill+\"&iframe=\"+iframe+\"&url=\"+url+\"&src=\"+src+\"&psa=\"+psa+\"&store=0\' style=\'display:none\'/>\"); }  document.write(\"<A target=\'_blank\' HREF=\'//madadsmedia.com\'>\"); document.write(\"<IMG SRC=\'//ads-by.madadsmedia.com/images/psa/728x90-psa.jpg\' BORDER=0 WIDTH=728 HEIGHT=90 ALT=\'Advertisement\'><\\/A>\");  </scr" + "ipt>";

// ======= DO NOT EDIT BELOW THIS LINE =========== //

var pbjs = pbjs || {};
pbjs.que = pbjs.que || [];

pbjs.bidderSettings = {
    rubicon: {
        bidCpmAdjustment: function(bidCpm) {
            return bidCpm * .85;
        }
    },
    pubmatic: {
        bidCpmAdjustment: function(bidCpm) {
            return bidCpm * .88;
        }
    },
};

(function() {
    var pbjsEl = document.createElement("script");
    pbjsEl.type = "text/javascript";
    pbjsEl.async = true;
    pbjsEl.src = "//ads-by.madadsmedia.com/js/prebid.js";
    var pbjsTargetEl = document.getElementsByTagName("head")[0];
    pbjsTargetEl.insertBefore(pbjsEl, pbjsTargetEl.firstChild);
})();

var doNotChange = 'doNotChange';
var ttID = null;
var ttID = document.getElementById('madcid').getAttribute('tt');

function loadAdUnit() {
pbjs.que.push(function() {
    var adUnits = [{
        code: doNotChange,
        sizes: [
            [tagWidth, tagHeight]
        ],
        bids: bids
    }];

    pbjs.addAdUnits(adUnits);

    pbjs.requestBids({
        timeout: bidTimeOut,
        bidsBackHandler: function() {
            var iframe = document.getElementById("728x90" + ttID);
            var iframeDoc = iframe.contentWindow.document;
            var params = pbjs.getAdserverTargetingForAdUnitCode(doNotChange);

           // If any bidders return any creatives, render the ad with the top bid.
            if (params && params['hb_adid'] && (params['hb_pb']) >= 0.07) {
                pbjs.renderAd(iframeDoc, params['hb_adid']);

            } else {
                // If no bidder return any creatives, run passback.
                iframe.width = tagWidth;
                iframe.height = tagHeight;
                var pb = document.getElementById("728x90" + ttID).contentWindow.document;
                pb.open();
                pb.write(passbackTagHtml);
                pb.close();
            }
        }
    });
});
if (document.getElementById("728x90" + ttID) == null) {
    document.write('<iframe id="728x90' + ttID + '" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" topmargin="0" leftmargin="0" width="0" height="0" sandbox="allow-same-origin allow-scripts allow-forms allow-popups"></iframe>');
}
}
(function () {
            var MdActiveAd = {
                config: {
                    adId: "",
                    userInactiveTimeout: 5,
                    nextAdTimeout: 15,
                    debug: false
                },
                vars: {
                    isActive: false,
                    timerHandle: null,
                    doc: null,
                    adEl: null,
                    window: null,
                    parentTT: null,
                    isInSight: false,
                    isWindowFocused: true,
                    lastActiveTime: 0,
                    ad: {
                        time: 0,
                        viewTime: 0
                    }
                },

                i: function (params) {
                    loadAdUnit();

                    if (typeof params.adId == "string") {
                        this.config.adId = params.adId;
                    }
                    if (typeof params.debug == "boolean") {
                        this.config.debug = params.debug;
                    }
                    if (typeof params.userInactiveTimeout == "number") {
                        this.config.userInactiveTimeout = params.userInactiveTimeout;
                    }
                    if (typeof params.nextAdTimeout == "number") {
                        this.config.nextAdTimeout = params.nextAdTimeout;
                    }

                    // Get parent salt Id
                    if (document.getElementById('madcid') == null) {
                        if (MdActiveAd.config.debug) {
                            MdActiveAd.debug('madcid - not found');
                        }
                    } else {
                        this.vars.parentTT = document.getElementById('madcid').getAttribute('tt');
                    }

                    // init elements
                    this.vars.window = window.parent;
                    this.vars.doc = window.parent.document;

                    MdActiveAd.config.adId = MdActiveAd.config.adId + this.vars.parentTT;

                    this.vars.adEl = this.vars.doc.getElementById(MdActiveAd.config.adId);
                    if (this.vars.adEl != null) {
                        this.setUserActive(true);
                        // init events
                        this.observeEvents();
                        // start timer
                        this.timer.start();
                    } else {
                        if (MdActiveAd.config.debug) {
                            MdActiveAd.debug('Ad container not found. ID: ' + MdActiveAd.config.adId);
                        }
                    }
                },

                setUserActive: function (state) {
                    if (MdActiveAd.config.debug) {
                        MdActiveAd.debug('Active user: ' + state);
                    }
                    this.vars.isActive = state;

                    if (this.vars.isActive) {
                        this.timer.start();
                    } else {
                        this.timer.stop();
                    }
                },

                timer: {
                    count: 0,
                    start: function () {
                        if (MdActiveAd.vars.timerHandle == null) {
                            MdActiveAd.vars.timerHandle = setInterval(this.event, 1000);
                        }
                    },
                    stop: function () {
                        if (MdActiveAd.vars.timerHandle != null) {
                            if (MdActiveAd.vars.timerHandle != null) {
                                clearInterval(MdActiveAd.vars.timerHandle);
                            }
                            MdActiveAd.vars.timerHandle = null;
                        }
                    },
                    event: function () {
                        MdActiveAd.timer.count++;
                        if (( MdActiveAd.timer.count - MdActiveAd.vars.lastActiveTime) >= MdActiveAd.config.userInactiveTimeout) {
                            MdActiveAd.setUserActive(false);
                        }

                        if (MdActiveAd.vars.isInSight) {
                            MdActiveAd.vars.ad.time++;
                            MdActiveAd.vars.ad.viewTime++;


                            if (MdActiveAd.vars.ad.time >= MdActiveAd.config.nextAdTimeout) {
                                MdActiveAd.vars.ad.time = 0;
                                MdActiveAd.vars.ad.count++;

                                // reload an Ad
                                loadAdUnit();

                                if (MdActiveAd.config.debug) {
                                    MdActiveAd.debug('load next an Ad: ID: ' + MdActiveAd.config.adId);
                                }
                            }
                        }
                    }
                },

                observeEvents: function () {
                    var eventsToObserve = ["mousemove", "mousedown", "scroll",
                        "keyup", "keydown",
                        "touchstart", "touchmove", "touchend",
                        "blur", "focus"];

                    for (var i = 0; i < eventsToObserve.length; i++) {
                        this.bindElementEvent(window.parent, eventsToObserve[i], function (event) {
                            //console.log("EVENT: " + event.type);
                            MdActiveAd.checkAdsInSight();

                            if (MdActiveAd.vars.isWindowFocused) {
                                MdActiveAd.vars.lastActiveTime = MdActiveAd.timer.count;
                            }

                            if (MdActiveAd.vars.isWindowFocused && !MdActiveAd.vars.isActive) {
                                MdActiveAd.setUserActive(true);
                            }

                            // Window focus
                            if (event.type == "focus") {
                                MdActiveAd.vars.lastActiveTime = MdActiveAd.timer.count;
                                MdActiveAd.vars.isWindowFocused = true;
                                MdActiveAd.setUserActive(true);
                                // MadScrollAd.Ad.checkAdsInSight();
                            } else if (event.type == "blur") {
                                MdActiveAd.vars.isWindowFocused = false;
                                MdActiveAd.setUserActive(false);
                            }

                        });
                    }
                },

                checkAdsInSight: function () {
                    var inSight = this.isOnView(this.vars.adEl);
                    //console.log("inSight: " + inSight + "   -  isInSight:" + this.vars.isInSight);
                    if (this.vars.isInSight != inSight) {
                        if (inSight) {
                            if (MdActiveAd.config.debug) {
                                MdActiveAd.debug("Ad on the screen. ID: " + this.vars.adEl.id);
                            }
                        } else {
                            if (MdActiveAd.config.debug) {
                                MdActiveAd.debug("Ad out the screen. ID: " + this.vars.adEl.id);
                            }
                        }
                    }

                    this.vars.isInSight = inSight;
                },

                isOnView: function (e) {

                    var offset = {x: 0, y: 0};
                    var width = e.clientWidth;
                    var height = e.clientHeight;
                    var elId = e.id;

                    while (e) {
                        offset.x += e.offsetLeft;
                        offset.y += e.offsetTop;
                        e = e.offsetParent;
                    }

                    if (MdActiveAd.vars.doc.documentElement && (MdActiveAd.vars.doc.documentElement.scrollTop || MdActiveAd.vars.doc.documentElement.scrollLeft)) {
                        offset.x -= MdActiveAd.vars.doc.documentElement.scrollLeft;
                        offset.y -= MdActiveAd.vars.doc.documentElement.scrollTop;
                    }
                    else if (MdActiveAd.vars.doc.body && (MdActiveAd.vars.doc.body.scrollTop || MdActiveAd.vars.doc.body.scrollLeft)) {
                        offset.x -= MdActiveAd.vars.doc.body.scrollLeft;
                        offset.y -= MdActiveAd.vars.doc.body.scrollTop;
                    }
                    else if (MdActiveAd.vars.window.pageXOffset || MdActiveAd.vars.window.pageYOffset) {
                        offset.x -= MdActiveAd.vars.window.pageXOffset;
                        offset.y -= MdActiveAd.vars.window.pageYOffset;
                    }
                    // //console.log(window);

                    //  console.log(elId + " " + offset.x + ' : ' + offset.y + "  H: " + height + " W:" + width + " innerHeight: " + window.innerHeight);

                    if (offset.y > (0 - (height / 2)) && offset.y < (MdActiveAd.vars.window.innerHeight - (height / 2))) {
                        return true;
                    } else {
                        return false;
                    }
                },

                bindElementEvent: function (element, type, handler) {
                    if (element.addEventListener) {
                        element.addEventListener(type, handler, false);
                    } else {
                        element.attachEvent("on" + type, handler);
                    }
                },
                debug: function (msg) {
                    console.log('MdActiveAd: ' + msg);
                }
            };

            MdActiveAd.i({
                adId: '728x90',
                userInactiveTimeout: 5,
                nextAdTimeout: 15,
                debug: true
            });
        })();