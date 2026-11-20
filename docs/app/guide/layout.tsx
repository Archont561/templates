import {DocsLayout} from 'fumadocs-ui/layouts/docs';
import {Blocks} from 'lucide-react';
import {source} from '@/lib/source';
export default function Layout({children}:{children:React.ReactNode}){return <DocsLayout tree={source.pageTree} nav={{title:<><Blocks size={19}/> Template Fieldnotes</>,url:'/'}} githubUrl="https://github.com/Archont561/templates">{children}</DocsLayout>}
