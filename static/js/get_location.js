function getLoc(store){
    var x, y
    if(store == "曲江书城") {
        x=108.982928,y=34.215148;
    }else if(store == "言几又") {
        x = 108.887213, y = 34.198026
    }else if(store == "中信书店") {
        x = 121.634155, y = 38.92413
    }else if(store == "止间书店") {
        x = 112.991576, y = 28.205118
    }
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
            // 百度地图API功能
            var map = new BMap.Map("container");
            var point = new BMap.Point(x,y);
            map.centerAndZoom(point,19);

            var geolocation = new BMap.Geolocation();
            // geolocation.getCurrentPosition(function(r){
            //     // if(this.getStatus() == BMAP_STATUS_SUCCESS){
            //     //     // var mk = new BMap.Marker(r.point);
            //     //     // map.addOverlay(mk);
            //     //     map.panTo(r.point);
            //     // }
            //     // else {
            //     //     alert('failed'+this.getStatus());
            //     // }
            // },{enableHighAccuracy: true})
        return;
    }
    alert("你的浏览器不支持获取地理位置！");
};

function showPosition(position){
    x=position.coords.latitude;
    y=position.coords.longitude;
}