var x=108.982928,y=34.215148;

window.onload = function() {
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