#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
float plota(vec2 st,float pct,float range){
    float v1=smoothstep(pct-range,pct,st.y);
    float v2=smoothstep(pct,pct+range,st.y);
    return v1-v2;
}
void main(){
    vec2 st=gl_FragCoord.xy/u_resolution;
    st*=4.;//aumenta a área de visualização
    st-=2.;//desloca o gráfico da função
    float y=sin(3.*st.x);
    // Desenha uma linha
    float valor=plota(st,y,.2);
    vec3 avec=vec3(.9451,.0549,.2471);
    vec3 cvec=vec3(1.,1.,1.);
    
    vec3 color=valor*avec;
    color=mix(color,avec,valor);
    valor=plota(st,y,.06);
    color=mix(color,cvec,valor);
    
    gl_FragColor=vec4(color,.8);
}