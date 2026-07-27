import streamlit as st
import streamlit.components.v1 as components
from common import GLOBAL_CSS
from data import PROFILE as profile, CERTIFICATIONS as certifications

st.set_page_config(page_title="Krishnendu Das | Portfolio", page_icon="🚀", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

hero_html = f"""
<div id="hero-canvas" style="width:100%;height:400px;position:relative;border-radius:16px;overflow:hidden;background:#05050a;cursor:pointer;">
  <canvas id="c3d" style="width:100%;height:100%;display:block;"></canvas>
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;pointer-events:none;background:radial-gradient(circle, rgba(5,5,10,0.1) 0%, rgba(5,5,10,0.8) 100%);">
    <h1 style="color:#fff;font-size:48px;margin:0;text-shadow:0 0 30px rgba(94,234,212,.8), 0 0 10px rgba(94,234,212,0.5);font-weight:bold;letter-spacing:1px;transition: transform 0.2s ease-out;" id="hero-title">{profile.get('name','')}</h1>
    <p style="color:#a8f0cb;font-size:18px;max-width:680px;margin-top:15px;text-shadow:0 0 10px rgba(168,240,203,0.5);">{profile.get('headline','')}</p>
  </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const canvas = document.getElementById('c3d');
const renderer = new THREE.WebGLRenderer({{canvas, alpha:true, antialias:true}});
renderer.setSize(canvas.clientWidth, canvas.clientHeight);
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, canvas.clientWidth/canvas.clientHeight, 0.1, 1000);
camera.position.z = 50;

// Interactive Particles
const particleCount = 1500;
const particlesGeo = new THREE.BufferGeometry();
const posArray = new Float32Array(particleCount * 3);
const velocityArray = new Float32Array(particleCount * 3);

for(let i=0; i < particleCount * 3; i++) {{
  posArray[i] = (Math.random() - 0.5) * 100;
  velocityArray[i] = (Math.random() - 0.5) * 0.05;
}}
particlesGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

const particleTexture = new THREE.TextureLoader().load('https://threejs.org/examples/textures/sprites/disc.png');
const particlesMat = new THREE.PointsMaterial({{
  size: 0.8,
  map: particleTexture,
  transparent: true,
  opacity: 0.8,
  color: 0x5eead4,
  blending: THREE.AdditiveBlending
}});

const particleMesh = new THREE.Points(particlesGeo, particlesMat);
scene.add(particleMesh);

// Center glowing geometric object
const geo = new THREE.TorusKnotGeometry(8, 2, 100, 16);
const mat = new THREE.MeshStandardMaterial({{ 
  color: 0x00ffcc, 
  wireframe: true, 
  emissive: 0x005544,
  emissiveIntensity: 0.5
}});
const torusKnot = new THREE.Mesh(geo, mat);
scene.add(torusKnot);

const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);
const pointLight = new THREE.PointLight(0x5eead4, 2, 100);
pointLight.position.set(10, 10, 10);
scene.add(pointLight);

// Mouse Interaction
let mouseX = 0;
let mouseY = 0;
let targetX = 0;
let targetY = 0;
const windowHalfX = canvas.clientWidth / 2;
const windowHalfY = canvas.clientHeight / 2;

document.getElementById('hero-canvas').addEventListener('mousemove', (event) => {{
  const rect = canvas.getBoundingClientRect();
  mouseX = (event.clientX - rect.left) - windowHalfX;
  mouseY = (event.clientY - rect.top) - windowHalfY;
  
  // Parallax effect on text
  const title = document.getElementById('hero-title');
  const moveX = (mouseX * 0.05);
  const moveY = (mouseY * 0.05);
  title.style.transform = `translate(${{moveX}}px, ${{moveY}}px)`;
}});

// Reset on mouse leave
document.getElementById('hero-canvas').addEventListener('mouseleave', () => {{
  mouseX = 0;
  mouseY = 0;
  const title = document.getElementById('hero-title');
  title.style.transform = `translate(0px, 0px)`;
}});

const clock = new THREE.Clock();

function animate() {{
  requestAnimationFrame(animate);
  const elapsedTime = clock.getElapsedTime();
  
  targetX = mouseX * 0.001;
  targetY = mouseY * 0.001;
  
  // Smooth rotation towards mouse
  torusKnot.rotation.y += 0.01 + (targetX - torusKnot.rotation.y) * 0.05;
  torusKnot.rotation.x += 0.01 + (targetY - torusKnot.rotation.x) * 0.05;
  
  // Particle wave motion
  const positions = particleMesh.geometry.attributes.position.array;
  for(let i = 0; i < particleCount; i++) {{
    const i3 = i * 3;
    const x = particleMesh.geometry.attributes.position.array[i3];
    positions[i3 + 1] += Math.sin(elapsedTime + x) * 0.02; // wave effect on Y
  }}
  particleMesh.geometry.attributes.position.needsUpdate = true;
  
  // Particle group rotation
  particleMesh.rotation.y += 0.002;
  particleMesh.rotation.x += (targetY - particleMesh.rotation.x) * 0.05;
  particleMesh.rotation.y += (targetX - particleMesh.rotation.y) * 0.05;
  
  renderer.render(scene, camera);
}}
animate();

window.addEventListener('resize', () => {{
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  camera.aspect = canvas.clientWidth / canvas.clientHeight;
  camera.updateProjectionMatrix();
}});
</script>
"""
components.html(hero_html, height=420)

st.markdown("## About")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("frontend/assets/profile.jpg", width=180)
with col2:
    st.markdown(f"### {profile.get('name','')}")
    st.markdown(f"**{profile.get('headline','')}**")
    st.write(profile.get("summary", ""))
    st.write(f"📍 {profile.get('location','')}  |  ✉️ {profile.get('email','')}  |  📞 {profile.get('phone','')}")
    st.write(f"[LinkedIn]({profile.get('linkedin','')})  •  [GitHub]({profile.get('github','')})")
    
    # Download Resume Button
    try:
        with open("frontend/assets/Krishnendu_Das_Resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Krishnendu_Das_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        pass

st.markdown("### Achievements")
st.markdown("""
- Built and deployed **7 independent projects** spanning AI automation, computer vision pipelines, browser extensions, and mobile apps
- Actively running a fully automated content pipeline publishing to live YouTube and Instagram channels
- Completed **4 certifications** in Generative AI, Machine Learning fundamentals, and RAG systems (Outskill, AWS, IBM SkillsBuild)
- Maintaining a CGPA of ~8.0/10 while building production-style projects alongside coursework
""")

st.markdown("## Skills")
skills = profile.get("skills", {})
cols = st.columns(len(skills) if skills else 1)
for col, (cat, items) in zip(cols, skills.items()):
    with col:
        st.markdown(f"**{cat}**")
        st.markdown("".join([f'<span class="badge">{s}</span>' for s in items]), unsafe_allow_html=True)

st.markdown("## Education")
st.write(profile.get("education", ""))

st.markdown("## Certifications")
if certifications:
    for c in certifications:
        st.markdown(f"- **{c['name']}** — {c['org']} ({c['year']})")
if not certifications:
    st.info("No certifications loaded.")

st.markdown("*(See the Projects and Contacts pages in the sidebar for more.)*")