// ex c

#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
uniform vec2 u_mouse;
void main(){
    vec2 st=gl_FragCoord.xy/u_resolution.xy;
    vec3 color=vec3(0.);
    vec2 m=u_mouse/u_resolution;
    if(m.y>.66){
        color=vec3(1.);
    }
    else if(m.y<=.66&&m.y>.33){
        color=vec3(.5);
    }
    else{
        color=vec3(0.);
    }
    gl_FragColor=vec4(color,1.);
}