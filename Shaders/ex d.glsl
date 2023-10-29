// ex c

#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
uniform vec2 u_mouse;
void main(){
    vec2 st = gl_FragCoord.xy/u_resolution.xy;
    
    float t = step(0.5,st.x);
    vec3 color = vec3(t,0.5,t);

    gl_FragColor = vec4(color, 1.0);
}