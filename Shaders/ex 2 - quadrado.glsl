#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
void main(){
    vec2 st=gl_FragCoord.xy/u_resolution.xy;
    vec3 color=vec3(0.);
    // bottom-left
    vec2 bl=step(vec2(.1),st);//simplificamos as operações em 1 única chamada
    // top-right
    vec2 tr=step(vec2(.1),1.-st);//invertemos a operação para cima e direita
    color=vec3(bl.x*bl.y*tr.x*tr.y);//operação AND
    gl_FragColor=vec4(color,1.);
}