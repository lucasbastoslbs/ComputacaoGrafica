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
    float valor=plota(st,y,.04);
    vec3 color_meio=valor*vec3(1.,1.,1.);
    valor=plota(st,y,.2);
    //vec3 color_fora=valor*vec3(0.96,0.2,0.26);
    vec3 color_fora=valor*vec3(.9451,.0549,.2471);
    
    //vec3 color = mix(color_meio, color_fora, vec3(0.8941, 0.0863, 0.302));
    vec3 color=mix(color_fora,color_meio,.3);
    
    gl_FragColor=vec4(color,.8);
}